from sqlalchemy import Column, Integer, Float, String

from database.database import Base


class BookDB(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    price = Column(Float)

    rating = Column(Integer)

    availability = Column(String)

    image_url = Column(String)

    product_url = Column(String)