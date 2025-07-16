import streamlit as st
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
from backend._scraper import scrape_article  # Mengimpor fungsi scrape_article dari scraper.py
from backend._trends import get_trends_data
from backend._prompt import create_title_prompt, create_meta_description_prompt, create_url_prompt
from groq import Groq
import os
from dotenv import load_dotenv
from db_crud import get_article_by_title, get_article_id_by_title, update_seo_recommendation, read_seo_recommendations

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mengambil API keys dari environment variables
api_key = os.getenv("API_KEY")
grog_api_key = os.getenv("GROG_API_KEY")

# Cek apakah API keys tersedia
if not api_key:
    st.error("API key untuk Google Trends tidak ditemukan. Pastikan Anda telah mengatur variabel lingkungan API_KEY.")
    st.stop()

if not grog_api_key:
    st.error("API key untuk Grog tidak ditemukan. Pastikan Anda telah mengatur variabel lingkungan GROG_API_KEY.")
    st.stop()

# Judul aplikasi
st.title("Rekomendasi On-Page SEO")

# Input URL artikel dari pengguna
user_url = st.text_input("Masukkan URL Artikel:")

# Tombol untuk mengeksekusi proses
if st.button('Process'):
    if not user_url:
        st.warning("Silakan masukkan URL artikel terlebih dahulu.")
    else:
        # Panggil fungsi scrape_article dari scraper.py
        data = scrape_article(user_url)

        if data:
            # Membersihkan teks artikel dari karakter yang tidak penting
            cleaned_text = " ".join(data[0]['isi'].split())  # Menghilangkan spasi berlebih
            cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,!?:;'\"-]", "", cleaned_text)  # Menghapus karakter yang tidak perlu

            # Menampilkan overview artikel setelah pembersihan
            st.subheader(f"Artikel: {data[0]['judul']}")
            st.text_area("Isi Artikel:", value=cleaned_text, height=300, disabled=True)

            # Ekstraksi kata kunci
            kw_model = KeyBERT(model=SentenceTransformer("all-mpnet-base-v2"))
            keywords = kw_model.extract_keywords(
                cleaned_text,
                keyphrase_ngram_range=(2, 2),
                use_mmr=True,
                diversity=0,
                top_n=5,
                stop_words='english'
            )

            # Tampilkan tabel hasil ekstraksi
            keyword_data = {
                "Nomor": [i + 1 for i in range(len(keywords))],
                "Keywords": [keyword for keyword, _ in keywords],
                "Cosine Similarity": [round(score, 4) for _, score in keywords]
            }
            df_keywords = pd.DataFrame(keyword_data)
            st.write("Top 5 Keywords:")
            st.dataframe(df_keywords)

            # Ambil data Google Trends
            trends_data, top_keyword = get_trends_data([keyword for keyword, _ in keywords], api_key)

            if not trends_data.empty:
                st.write("Interest Over Time (30 Hari Terakhir - Global):")
                st.dataframe(trends_data)
                st.write(f"Kata Kunci dengan Interest Tertinggi: **{top_keyword['keyword']}**")
                st.write(f"Interest Score: **{top_keyword['average_search_volume']}**")

                # Siapkan prompt
                content = cleaned_text
                keyword = top_keyword['keyword']
                title_prompt = create_title_prompt(content, keyword)
                meta_description_prompt = create_meta_description_prompt(content, keyword)
                url_prompt = create_url_prompt(content, keyword)

                # Buat client Grog
                client = Groq(api_key=grog_api_key)

                try:
                    title_response = client.chat.completions.create(
                        messages=[{"role": "user", "content": title_prompt}],
                        model="llama-3.3-70b-versatile",
                        stream=False,
                    )
                    meta_description_response = client.chat.completions.create(
                        messages=[{"role": "user", "content": meta_description_prompt}],
                        model="llama-3.3-70b-versatile",
                        stream=False,
                    )
                    url_response = client.chat.completions.create(
                        messages=[{"role": "user", "content": url_prompt}],
                        model="llama-3.3-70b-versatile",
                        stream=False,
                    )

                    # Tampilkan hasil dari Grog API
                    st.subheader("Hasil Optimasi SEO:")

                    st.markdown("**Title:**")
                    st.write(title_response.choices[0].message.content)

                    st.markdown("**Meta Description:**")
                    st.write(meta_description_response.choices[0].message.content)

                    st.markdown("**URL:**")
                    st.write(url_response.choices[0].message.content)

                    # Simpan ke DB
                    try:
                        update_seo_recommendation(
                            article_id=get_article_id_by_title(data[0]['judul']),
                            recommended_title=title_response.choices[0].message.content,
                            recommended_meta_description=meta_description_response.choices[0].message.content,
                            recommended_url=url_response.choices[0].message.content,
                            keyword=top_keyword['keyword'],
                            popularity_score=float(top_keyword['average_search_volume'])
                        )
                        st.success("Data rekomendasi SEO berhasil disimpan ke database.")
                    except Exception as e:
                        st.error(f"Gagal menyimpan data ke database: {e}")

                except Exception as e:
                    st.error(f"Terjadi kesalahan saat menghubungi Grog API: {e}")

                # Tampilkan riwayat rekomendasi
                st.subheader("Riwayat Rekomendasi SEO untuk Artikel Ini:")
                rows = read_seo_recommendations(get_article_id_by_title(data[0]['judul']))
                if rows:
                    df = pd.DataFrame(rows, columns=[
                        "Title", "Meta Description", "URL", "Keyword", "Popularity Score", "Created At"
                    ])
                    st.dataframe(df)
                else:
                    st.info("Belum ada data rekomendasi SEO untuk artikel ini.")
            else:
                st.warning("Data tren tidak tersedia untuk kata kunci yang diekstrak.")
        else:
            st.warning("Artikel tidak ditemukan atau terjadi kesalahan.")
