import sqlite3

DB_PATH = "projeto.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_sqlite():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            estado TEXT,
            pais TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_city(nome, estado, pais):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO cidades (nome, estado, pais) VALUES (?, ?, ?)", (nome, estado, pais))
    conn.commit()
    conn.close()

def list_cities():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, estado, pais FROM cidades")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_city_by_id(cid):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, estado, pais FROM cidades WHERE id=?", (cid,))
    row = cur.fetchone()
    conn.close()
    return row
