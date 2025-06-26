import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
from backend._trends import get_trends_data
from backend._prompt import create_title_prompt, create_meta_description_prompt, create_url_prompt
from groq import Groq
import os
from dotenv import load_dotenv

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

# Input teks dari pengguna
doc = st.text_area("Input Content:")

# Inisialisasi KeyBERT dengan model SentenceTransformer
kw_model = KeyBERT(model=SentenceTransformer("all-mpnet-base-v2"))

# Tombol untuk mengeksekusi proses
if st.button('Process'):
    if doc:
        # Ekstraksi kata kunci
        keywords = kw_model.extract_keywords(
            doc,
            keyphrase_ngram_range=(2, 2),
            use_mmr=True,
            diversity=0,
            top_n=5,
            stop_words='english'
        )

        # Tampilkan tabel hasil ekstraksi
        data = {
            "Nomor": [i + 1 for i in range(len(keywords))],
            "Keywords": [keyword for keyword, _ in keywords],
            "Cosine Similarity": [round(score, 4) for _, score in keywords]
        }
        df_keywords = pd.DataFrame(data)
        st.write("Top 5 Keywords:")
        st.dataframe(df_keywords)

        # Ambil data Google Trends
        trends_data, top_keyword = get_trends_data([keyword for keyword, _ in keywords], api_key)

        if not trends_data.empty:
            st.write("Interest Over Time (30 Hari Terakhir - Global):")
            st.dataframe(trends_data)
            st.write(f"Kata Kunci dengan Interest Tertinggi: **{top_keyword['keyword']}**")

            # Siapkan prompt
            content = doc
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

            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghubungi Grog API: {e}")
        else:
            st.warning("Data tren tidak tersedia untuk kata kunci yang diekstrak.")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu sebelum mengekstrak.")