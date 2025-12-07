

import sqlite3
from typing import Optional
from models import PriceChange

class Database:
    def __init__(self, path: str) -> None:
        self.conn = sqlite3.connect(path)

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS products ("
            "name TEXT PRIMARY KEY,"
            "last_price TEXT NOT NULL)"
        )

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS price_changes ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "product_name TEXT NOT NULL,"
            "old_price TEXT NOT NULL,"
            "new_price TEXT NOT NULL,"
            "time TEXT NOT NULL)"
        )

        self.conn.commit()

    def get_last_price(self, name: str) -> Optional[str]:
        cur = self.conn.execute("SELECT last_price FROM products WHERE name=?", (name,))
        row = cur.fetchone()
        return row[0] if row else None

    def upsert_price(self, name: str, price: str) -> None:
        if self.get_last_price(name) is None:
            self.conn.execute("INSERT INTO products (name, last_price) VALUES (?, ?)", (name, price))
        else:
            self.conn.execute("UPDATE products SET last_price=? WHERE name=?", (price, name))
        self.conn.commit()

    def record_change(self, change: PriceChange) -> None:
        self.conn.execute(
            "INSERT INTO price_changes (product_name, old_price, new_price, time) "
            "VALUES (?, ?, ?, ?)",
            (change.product_name, change.old_price, change.new_price, change.time.isoformat())
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()