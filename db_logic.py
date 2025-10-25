import sqlite3

from config import *

class DB():
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)

    def create_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, password TEXT NOT NULL)")

    def add_user(self, tg_id, password):
        pass

    def add_money(self, category):
        pass

    def remove_money(self, category):
        pass
