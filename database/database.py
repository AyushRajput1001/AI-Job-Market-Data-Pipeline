from sqlalchemy import create_engine # sqlalchemy ORM (object relational mapper)
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) # connects py to db

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

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

    print("Books table created successfully!")