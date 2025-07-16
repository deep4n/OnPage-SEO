# db_crud.py
import psycopg2
import os
from dotenv import load_dotenv
import re

load_dotenv()

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    
# Fungsi untuk menambahkan data artikel ke dalam tabel `articles`
def create_article(title, content, url, meta_description):
    # content = re.sub(r'\n\s*\n', r'\\n', content)
    content = content.replace('\n', '\\n')
    print(content)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO articles (title, content, url, meta_description)
           VALUES (%s, %s, %s, %s)""",
        (title, content, url, meta_description)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Artikel '{title}' berhasil disimpan.")

def get_content_by_article_id(article_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT content FROM articles WHERE id = %s", (article_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def get_article_by_title(title):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT content FROM articles WHERE title = %s", (title,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result  # result[0]=id, result[1]=content jika ditemukan, None jika tidak

def get_all_article_titles():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT original_title FROM articles ORDER BY original_title")
    results = cur.fetchall()
    results = [row[0] for row in results]
    cur.close()
    conn.close()
    return results
    
def create_seo_recommendation(article_id, recommended_title, recommended_meta_description, recommended_url, keyword, popularity_score):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO seo_recommendations
           (article_id, recommended_title, recommended_meta_description, recommended_url, keyword, popularity_score)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (article_id, recommended_title, recommended_meta_description, recommended_url, keyword, popularity_score)
    )
    conn.commit()
    cur.close()
    conn.close()
    
def update_seo_recommendation(article_id, recommended_title, recommended_meta_description, recommended_url, keyword, popularity_score):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE seo_recommendations
        SET recommended_title = %s,
            recommended_meta_description = %s,
            recommended_url = %s,
            keyword = %s,
            popularity_score = %s,
            created_at = NOW()
        WHERE article_id = %s
    """, (recommended_title, recommended_meta_description, recommended_url, keyword, popularity_score, article_id))
    conn.commit()
    cur.close()
    conn.close()

def read_seo_recommendations(article_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT recommended_title, recommended_meta_description, recommended_url, keyword, popularity_score, created_at FROM seo_recommendations WHERE article_id = %s ORDER BY created_at DESC", (article_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_article_id_by_title(title):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM articles WHERE title = %s", (title,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row[0] if row else None
    return row[0] if row else None


