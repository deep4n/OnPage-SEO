import streamlit as st
import pandas as pd
from keybert import KeyBERT
from backend._trends import get_trends_data  # Impor fungsi dari backend
from backend._grog import get_grog_response  # Impor fungsi dari backend
from groq import Groq
import os

# Judul aplikasi
st.title("Keyword Extraction and Google Trends")

# Deskripsi aplikasi
st.write("""
    Aplikasi ini menggunakan model **KeyBERT** untuk mengekstraksi kata kunci dari dokumen dan mengambil data
    "interest over time" dari Google Trends berdasarkan kata kunci yang diekstrak dalam 30 hari terakhir secara global.
    Anda bisa memasukkan dokumen di bawah ini dan tekan tombol untuk melihat kata kunci yang diekstrak dan
    data "interest over time" untuk kata kunci tersebut.
""")

# Menyediakan input teks untuk pengguna
doc = st.text_area("Masukkan dokumen atau teks untuk ekstraksi kata kunci:")

# Membuat model KeyBERT
kw_model = KeyBERT()

# Tombol untuk memulai ekstraksi
if st.button('Ekstrak Kata Kunci'):
    if doc:  # Jika dokumen tidak kosong
        # Ekstraksi kata kunci
        keywords = kw_model.extract_keywords(doc)
        
        # Menyusun data dalam format tabel untuk kata kunci
        data = {
            "Nomor": [i + 1 for i in range(len(keywords))],
            "Keywords": [keyword for keyword, score in keywords],
            "Cosine Similarity": [score for keyword, score in keywords]
        }
        
        # Membuat DataFrame untuk kata kunci
        df_keywords = pd.DataFrame(data)
        st.write("Top 5 Keywords:")
        st.table(df_keywords)  # Tampilkan tabel kata kunci
        
        # Ambil data interest over time untuk setiap kata kunci
        api_key = "13b874b099de271f564b31c07c2a652f2e7c697586cfa8e512ba870bbfdc42c8"  # Ganti dengan kunci API SERP Anda
        trends_data, top_keyword = get_trends_data([keyword for keyword, _ in keywords], api_key)
        
        # Periksa jika data trends_data kosong
        if not trends_data.empty:
            st.write("Interest Over Time (30 Hari Terakhir - Global):")
            st.dataframe(trends_data)  # Tampilkan data dalam bentuk tabel
            
            # Menampilkan kata kunci dengan interest tertinggi
            st.write(f"Kata Kunci dengan Interest Tertinggi: {top_keyword['keyword']}")
            
            # Buat Prompt untuk Grog API (title, meta description, dan URL)
            content = doc
            keyword = top_keyword['keyword']
            
            # API key Grog API
            # Menyediakan API key Grog secara langsung
            grog_api_key = "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"  # Ganti dengan API key yang Anda dapatkan dari Grog

            # Membuat client Grog
            client = Groq(api_key=grog_api_key)

            # Membuat prompt untuk title, meta description, dan URL
            title_prompt = f"Generate an SEO-friendly title based on this content: {content}. The main keyword is {keyword}."
            meta_description_prompt = f"Generate an SEO meta description for this content: {content}. The main keyword is {keyword}."
            url_prompt = f"Generate an SEO-friendly URL for this content: {content}. The main keyword is {keyword}."

            # Mengirimkan prompt ke Grog API dan mendapatkan respons
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

            # Menampilkan hasil respons dari Grog API
            st.write("Generated Title:")
            st.write(title_response.choices[0].message.content)

            st.write("\nGenerated Meta Description:")
            st.write(meta_description_response.choices[0].message.content)

            st.write("\nGenerated URL:")
            st.write(url_response.choices[0].message.content)
            
        else:
            st.write("Data tidak ditemukan untuk kata kunci tersebut.")
        
    else:
        st.write("Masukkan teks untuk melihat hasil ekstraksi kata kunci.")
