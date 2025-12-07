

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    name: str
    price: str

@dataclass
class PriceChange:
    product_name: str
    old_price: str
    new_price: str
    time: datetime