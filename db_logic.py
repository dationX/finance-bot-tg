import sqlite3

from config import *
from funcs import *

class DB():
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)

    def create_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER NOT NULL UNIQUE, money INTEGER NOT NULL)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS history_money(user_id INTEGER,money_value TEXT NOT NULL, category TEXT NOT NULL, time DATETIME)")

    def add_user(self, tg_id):
        try:
            self.conn.execute(f"""
                INSERT INTO users VALUES
                    ({tg_id}, 0)
                """)
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass
        
    def add_money(self, tg_id, money, category, time):
        values = (tg_id, money, category, time)

        self.conn.execute(f"""
            INSERT INTO history_money VALUES
                (?, ?, ?, ?)
            """, values)
        
        self.conn.commit()

        self.update_money(tg_id)


    def update_money(self, tg_id):
        """Update column money in table users"""

        cur = self.conn.cursor()
        cur.execute(f"""SELECT money_value FROM history_money
                    WHERE user_id = {tg_id};
                    """)
        
        data = cur.fetchall()
        money = 0
        for value in data:
            money += int(value[0])

        cur.execute(f"""
            UPDATE users
            set money = {money}
            WHERE user_id = {tg_id}
            """)
        
        self.conn.commit()

    def reset(self, tg_id):
        self.conn.execute(f"DELETE FROM history_money WHERE history_money.user_id = {tg_id}")
        self.update_money(tg_id)

    def info_money(self, tg_id):
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT money FROM users
            WHERE user_id = {tg_id}
            """)
        
        money = cur.fetchall()[0]

        return money
    
    def info_money_category(self, tg_id):
        cur = self.conn.cursor()
    
        cur.execute(f"""SELECT money_value, category, time FROM history_money
                        WHERE user_id = {tg_id}""")
        
        return cur.fetchall()
        