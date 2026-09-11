from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    price: float
    rating: int
    availability: str
    image_url: str
    product_url: str

    class Config:
        from_attributes = True