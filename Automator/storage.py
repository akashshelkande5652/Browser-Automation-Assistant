#This code creates a simple database system to track website testing runs,
# storing the site name, status, any messages, screenshot data, and timestamps.


import sqlite3
from contextlib import closing
from datetime import datetime

def init_db(db_path="results.db"):
    with closing(sqlite3.connect(db_path)) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT,
            status TEXT,
            message TEXT,
            screenshot TEXT,
            created_at TEXT
        );
        """)
        conn.commit()

def save_result(db_path, site, status, message, screenshot):
    with closing(sqlite3.connect(db_path)) as conn:
        conn.execute(
            "INSERT INTO runs (site, status, message, screenshot, created_at) VALUES (?,?,?,?,?);",
            (site, status, message, screenshot, datetime.utcnow().isoformat())
        )
        conn.commit()
