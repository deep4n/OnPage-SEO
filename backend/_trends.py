import requests
import pandas as pd

def get_trends_data(keywords, api_key):
    """
    Mengambil data 'interest over time' dari Google Trends menggunakan SERP API
    dalam 30 hari terakhir secara global dan mengambil rata-rata pencarian yang sudah disediakan
    oleh API untuk setiap kata kunci.
    
    Arguments:
        keywords: List of keywords to search for (e.g., ["python", "machine learning"])
        api_key: Your SERP API key for accessing Google Trends data.
        
    Returns:
        Pandas DataFrame with 'interest over time' data and average search volume.
    """
    trends_data = []

    # Menggabungkan kata kunci dalam format yang sesuai
    keywords_str = ",".join(keywords)
    
    # Menyiapkan parameter untuk SERP API
    params = {
        "engine": "google_trends",  # Menyatakan bahwa kita ingin menggunakan Google Trends
        "q": keywords_str,  # Daftar kata kunci
        "hl": "en",  # Bahasa (English)
        "date": "today 1-m",  # 30 hari terakhir
        "cat": "0",
        "tz": "-540",  # Zona waktu (UTC -9 jam)
        "data_type": "TIMESERIES",  # Data dalam bentuk time series (interest over time)
        "api_key": api_key  # Kunci API untuk autentikasi
    }

    # Mengirim permintaan ke SERP API
    url = "https://serpapi.com/search.json"
    response = requests.get(url, params=params)
    results = response.json()

    # Memeriksa apakah data interest_over_time ada dalam respons
    if "interest_over_time" in results:
        # Menyusun data interest over time dalam bentuk DataFrame
        timeline_data = results["interest_over_time"]["timeline_data"]
        for entry in timeline_data:
            date = entry["date"]
            for value in entry["values"]:
                keyword = value["query"]
                trends_data.append({
                    "keyword": keyword,
                    "date": date,
                    "value": value["value"]
                })
    else:
        return pd.DataFrame()  # Kembalikan DataFrame kosong jika tidak ada data
    
    # Membuat DataFrame dari data yang diperoleh
    df = pd.DataFrame(trends_data)

    # Pastikan kolom 'value' berisi data numerik, jika tidak, ubah menjadi numerik
    df['value'] = pd.to_numeric(df['value'], errors='coerce')  # 'coerce' akan mengganti nilai yang tidak bisa dikonversi dengan NaN

    # Debugging: Cek data yang dikumpulkan
    print("Data yang dikumpulkan:", df.head())  # Menampilkan data yang telah dikumpulkan

    # Mengambil data rata-rata dari hasil JSON jika tersedia
    if "interest_over_time" in results and "averages" in results["interest_over_time"]:
        averages = results["interest_over_time"]["averages"]
        
        # Mengubah averages menjadi DataFrame untuk memudahkan manipulasi
        averages_df = pd.DataFrame(averages)
        
        # Menyusun ulang kolom menjadi 'keyword' dan 'average_search_volume'
        averages_df = averages_df.rename(columns={"query": "keyword", "value": "average_search_volume"})
        
        # Debugging: Menampilkan rata-rata yang diperoleh dari JSON
        print("Averages from API:", averages_df)

        # Menentukan kata kunci dengan rata-rata tertinggi
        top_keyword = averages_df.loc[averages_df['average_search_volume'].idxmax()]

        # Menampilkan kata kunci dengan rata-rata tertinggi
        print(f"Kata Kunci dengan Rata-rata Tertinggi: {top_keyword['keyword']}")
        print(f"Rata-rata Pencarian: {top_keyword['average_search_volume']}")

        return averages_df[['keyword', 'average_search_volume']], top_keyword  # Mengembalikan DataFrame dan kata kunci dengan rata-rata tertinggi
    else:
        print("Tidak ada data rata-rata yang ditemukan dalam respons.")
        return pd.DataFrame(), None  # Kembalikan DataFrame kosong jika tidak ada rata-rata yang ditemukan
