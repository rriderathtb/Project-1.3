import sqlite3
import datetime

class Logger:
    def __init__(self, db_path="preventx_log.db"):
        self.db_path = db_path
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                attack_type TEXT,
                mac_address TEXT,
                details TEXT
            )
        """)
        conn.commit()
        conn.close()

    def log(self, attack_type, mac, details=""):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        c.execute(
            "INSERT INTO logs (timestamp, attack_type, mac_address, details) VALUES (?, ?, ?, ?)",
            (timestamp, attack_type, mac, details),
        )
        conn.commit()
        conn.close()