import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from db_crud import create_article  # Mengimpor fungsi create_article dari db_crud.py

# Setup headless Chrome
def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Menjalankan di background (tanpa UI)
    driver = webdriver.Chrome(options=options)
    return driver

# Fungsi untuk melakukan scraping artikel
def scrape_article(user_url):
    driver = create_driver()
    wait = WebDriverWait(driver, 10)
    data = []

    try:
        # Pastikan URL valid dan mengarah ke artikel
        if "https://tujuhsembilan.com/article/detail" not in user_url:
            print("URL tidak valid. URL harus mengarah ke halaman artikel di https://tujuhsembilan.com/article/detail")
            return None
        
        # Buka halaman artikel dari URL input pengguna
        driver.get(user_url)
        
        # Tunggu hingga elemen utama yang menunjukkan artikel dimuat
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # Verifikasi URL yang dimuat
        current_url = driver.current_url
        if current_url != user_url:
            print(f"URL yang dimuat berbeda. Diharapkan: {user_url}, tetapi yang dimuat adalah: {current_url}")
            
            # Jika halaman utama dimuat, alihkan ke halaman daftar artikel
            if current_url == "https://tujuhsembilan.com/":
                print("Halaman utama dimuat, mengalihkan ke halaman artikel...")
                driver.get("https://tujuhsembilan.com/article/")
                time.sleep(3)
                
                # Ambil semua link artikel di halaman daftar artikel
                soup = BeautifulSoup(driver.page_source, "html.parser")
                article_links = soup.select('a[href^="/article/detail"]')

                # Cari artikel yang sesuai dengan URL yang dimasukkan
                found_article = False
                for a in article_links:
                    article_url = "https://tujuhsembilan.com" + a['href']
                    if article_url == user_url:
                        print(f"Artikel ditemukan di daftar: {article_url}")
                        driver.get(article_url)
                        time.sleep(3)
                        found_article = True
                        break
                
                if not found_article:
                    print("Artikel tidak ditemukan di halaman daftar.")
                    return None
            
        else:
            print(f"URL yang dimuat adalah: {current_url}")

        # Scraping artikel dari URL input pengguna
        print(f"\nScraping halaman: {current_url}")
        time.sleep(2)

        # Scraping judul dan isi artikel
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Ambil meta description
        meta_description_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = meta_description_tag["content"] if meta_description_tag else "Tidak ada deskripsi"

        # Ambil judul artikel
        title_tag = soup.find("h1")

        # Ambil semua elemen <h3> dan <p> dalam urutan yang benar
        content_list = []
        elements = soup.find_all(["p", "h3", "h4"])

        for element in elements:
            # Tambahkan teks dari setiap elemen yang ditemukan
            content_list.append(element.get_text(strip=True))
            
        # Gabungkan semua konten dalam urutan yang benar
        content = "\n".join(content_list)

        if not title_tag or not content:
            print("Artikel kosong atau tidak lengkap.")
            return None

        title = title_tag.get_text(strip=True)

        # Simpan data ke database menggunakan fungsi save_to_db dari db_crud.py
        create_article(title, content, user_url, meta_description)
        
        data.append({
            'judul': title,
            'isi': content,
            'url_pengguna': user_url,
            'deskripsi_meta': meta_description
        })

        print(f"\nTotal artikel disimpan ke database: {len(data)}")

    finally:
        driver.quit()

    return data
