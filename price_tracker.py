

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List

from models import Product, PriceChange
from database import Database
from tracker_base import Tracker

class PriceTracker(Tracker):
    def __init__(self, db: Database, url: str):
        self.db = db
        self.url = url

    def scrape_products(self) -> List[Product]:
       
        a
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")


        cards = soup.select(".product")

        products = []
        for card in cards:
            name_tag = card.find("h3")
            price_tag = card.find("p", class_="price")

            if name_tag and price_tag:
                products.append(
                    Product(
                        name=name_tag.get_text(strip=True),
                        price=price_tag.get_text(strip=True)
                    )
                )

        return products

    def run_once(self) -> None:
             
        
        products = self.scrape_products()

        if not products:
            print("No products found.")
            return

        print("Current product prices:")
        print("----------------------")

        for p in products:
            print(f"{p.name:<20} -> {p.price}")

            last_price = self.db.get_last_price(p.name)

            if last_price is None:
                self.db.upsert_price(p.name, p.price)
            elif last_price != p.price:
                change = PriceChange(
                    product_name=p.name,
                    old_price=last_price,
                    new_price=p.price,
                    time=datetime.now()
                )
                self.db.record_change(change)
                self.db.upsert_price(p.name, p.price)
