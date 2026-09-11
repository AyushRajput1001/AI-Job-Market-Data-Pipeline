import sqlite3
import pandas as pd

class BookAnalyzer:

    def __init__(self):
        self.database = "database/books.db"

    def connect(self):
        return sqlite3.connect(self.database)

    def average_price(self):

        connection = self.connect()

        query = "SELECT AVG(price) FROM books"

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def highest_price(self):

        connection = self.connect()

        query = "SELECT MAX(price) FROM books"

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    query = """
    SELECT *
    FROM books
    WHERE rating = 5
    """
    
    def total_books(self):

        connection = self.connect()

        query = """
        SELECT COUNT(*) AS TotalBooks
        FROM books
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def average_price(self):

        connection = self.connect()

        query = """
        SELECT AVG(price) AS AveragePrice
        FROM books
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    def highest_price(self):

        connection = self.connect()

        query = """
        SELECT MAX(price) AS HighestPrice
        FROM books
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def lowest_price(self):

        connection = self.connect()

        query = """
        SELECT MIN(price) AS LowestPrice
        FROM books
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    def five_star_books(self):

        connection = self.connect()

        query = """
        SELECT *
        FROM books
        WHERE rating = 5
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def expensive_books(self):

        connection = self.connect()

        query = """
        SELECT *
        FROM books
        WHERE price > 50
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def books_by_rating(self):

        connection = self.connect()

        query = """
        SELECT
            rating,
            COUNT(*) AS total_books
        FROM books
        GROUP BY rating
        ORDER BY rating
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def average_price_by_rating(self):

        connection = self.connect()

        query = """
        SELECT
            rating,
            AVG(price) AS average_price
        FROM books
        GROUP BY rating
        ORDER BY rating
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def top_expensive_books(self):

        connection = self.connect()

        query = """
        SELECT
            title,
            price,
            rating
        FROM books
        ORDER BY price DESC
        LIMIT 10
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def cheapest_books(self):

        connection = self.connect()

        query = """
        SELECT
            title,
            price,
            rating
        FROM books
        ORDER BY price ASC
        LIMIT 10
        """

        result = pd.read_sql(query,connection)

        connection.close()

        return result
    
    def available_books(self):

        connection = self.connect()

        query = """
        SELECT COUNT(*) AS available_books
        FROM books
        WHERE availability = 'In stock'
        """
        result = pd.read_sql(query,connection)

        connection.close()

        return result
    
    def highest_rated_books(self):

        connection = self.connect()

        query = """
        SELECT
            title,
            price,
            rating
        FROM books
        WHERE rating = 5
        ORDER BY price DESC
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result

    def books_above_average_price(self):

        connection = self.connect()

        query = """
        SELECT
            title,
            price,
            rating
        FROM books
        WHERE price >
        (
            SELECT AVG(price)
            FROM books
        )
        ORDER BY price DESC
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result
    
    def books_below_average_price(self):

        connection = self.connect()

        query = """
        SELECT
            title,
            price,
            rating
        FROM books
        WHERE price <
        (
            SELECT AVG(price)
            FROM books
        )
        ORDER BY price ASC
        """

        result = pd.read_sql(query, connection)

        connection.close()

        return result