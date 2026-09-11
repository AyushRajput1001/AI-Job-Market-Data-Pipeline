from database.database import SessionLocal
from database.models import BookDB

class ORMManager:

    def __init__(self):
        self.session = SessionLocal()

    def insert_book(self, book):

        db_book = BookDB(

            title=book["Title"],
            price=book["Price"],
            rating=book["Rating"],
            availability=book["Availability"],
            image_url=book["Image URL"],
            product_url=book["Product URL"]

        )

        self.session.add(db_book)

    def commit(self):

        self.session.commit()

    def close(self):

        self.session.close()

    def get_all_books(self):

        return self.session.query(BookDB).all()