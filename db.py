import sqlite3 as sq

class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def create_trable(self):
        with self.connection:
            self.cursor.execute(("""CREATE TABLE IF NOT EXISTS data (
                                    user_id INTEGER,
                                    username TEXT NOT NULL,
                                    first_name TEXT DEFAULT none,
                                    last_name TEXT DEFAULT none,
                                    premium INTEGER DEFAULT 0
                                    )"""))
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM data WHERE user_id = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
        
    def add_user(self, user_id, username, first_n, last_n, premium):
        with self.connection:
            self.cursor.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?)", (user_id, username, first_n, last_n, premium,))