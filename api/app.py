from fastapi import FastAPI
from database.database import SessionLocal
from database.models import BookDB
from fastapi import Query
from api.schemas import BookSchema
from typing import List
from sqlalchemy import asc, desc
from typing import List
from fastapi import HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Book API"}




@app.get("/books", response_model=List[BookSchema])
def get_books(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):

    session = SessionLocal()

    books = (
        session.query(BookDB)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    session.close()

    return books

@app.get("/books/sort", response_model=List[BookSchema])
def sort_books(
    by: str = "price",
    order: str = "asc"
):

    session = SessionLocal()

    query = session.query(BookDB)

    if by == "price":
        if order == "asc":
            query = query.order_by(asc(BookDB.price))
        else:
            query = query.order_by(desc(BookDB.price))

    elif by == "rating":
        if order == "asc":
            query = query.order_by(asc(BookDB.rating))
        else:
            query = query.order_by(desc(BookDB.rating))

    books = query.all()

    session.close()

    return books

@app.get("/books/{book_id}", response_model=BookSchema)
def get_book(book_id: int):

    session = SessionLocal()

    book = (
        session.query(BookDB)
        .filter(BookDB.id == book_id)
        .first()
    )

    session.close()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

@app.get("/books/rating/{rating}", response_model=List[BookSchema])
def get_books_by_rating(rating: int):

    session = SessionLocal()

    books = session.query(BookDB).filter(BookDB.rating == rating).all()

    session.close()

    return books

@app.get("/books/price", response_model=List[BookSchema])
def get_books_by_price(
    min: float = Query(0),
    max: float = Query(1000)
):

    session = SessionLocal()

    books = (
        session.query(BookDB)
        .filter(BookDB.price >= min)
        .filter(BookDB.price <= max)
        .all()
    )

    session.close()

    return books

@app.get("/books/search", response_model=List[BookSchema])
def search_books(title: str):

    session = SessionLocal()

    books = (
        session.query(BookDB)
        .filter(BookDB.title.ilike(f"%{title}%"))
        .all()
    )

    session.close()

    return books

@app.get("/books/sort", response_model=List[BookSchema])
def sort_books(
    by: str = "price",
    order: str = "asc"
):

    session = SessionLocal()

    query = session.query(BookDB)

    if by == "price":
        if order == "asc":
            query = query.order_by(asc(BookDB.price))
        else:
            query = query.order_by(desc(BookDB.price))

    elif by == "rating":
        if order == "asc":
            query = query.order_by(asc(BookDB.rating))
        else:
            query = query.order_by(desc(BookDB.rating))

    books = query.all()

    session.close()

    return books