import sqlite3
from config.logger import logger

class DatabaseManager:

    def __init__(self):
        self.database = "database/books.db"

    def connect(self):
        connection = sqlite3.connect(self.database)
        return connection

    def create_table(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            price REAL,

            rating INTEGER,

            availability TEXT,

            image_url TEXT,

            product_url TEXT

        )
        """)

        connection.commit()

        connection.close()

        logger.info("Books table created successfully!")

    def insert_books(self, df):

        connection = self.connect()

        cursor = connection.cursor()

        for _, row in df.iterrows():

            cursor.execute("""
            INSERT INTO books
            (
                title,
                price,
                rating,
                availability,
                image_url,
                product_url
            )

            VALUES (?, ?, ?, ?, ?, ?)

            """,

            (
                row["Title"],
                row["Price"],
                row["Rating"],
                row["Availability"],
                row["Image URL"],
                row["Product URL"]
            )
            )

        connection.commit()

        connection.close()

        logger.info("Books inserted successfully!")