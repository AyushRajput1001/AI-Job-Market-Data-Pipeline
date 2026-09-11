from dataclasses import dataclass

@dataclass
class Book:
    title: str
    price: float
    rating: int
    availability: str
    image_url: str
    product_url: str