import csv
import requests
from models.book import Book
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config.logger import logger

class BookScraper:
    
    def __init__(self):
        self.url = "https://books.toscrape.com/"
    
    BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
    TOTAL_PAGES = 50

    def fetch_page(self,url):
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def scrape(self):
        books = []
        for page in range(1,self.TOTAL_PAGES+1):

            url = self.BASE_URL.format(page)

            logger.info(f"Scraping Page {page}")

            soup = self.fetch_page(url)

            books_html = soup.find_all("article")
            print(f"Page {page}: Found {len(books_html)} books")

            for book in books_html:

                title = book.h3.a["title"]

                price = book.find("p", class_="price_color").text.replace("Â£", "£")
                price = price.replace("£","")
                price = float(price)
                rating = book.find("p", class_="star-rating")["class"][1]
                if rating == "One":
                    rating = 1
                elif rating == "Two":
                    rating = 2
                elif rating == "Three":
                    rating = 3
                elif rating == "Four":
                    rating = 4
                else:
                    rating = 5


                availability = book.find("p", class_="instock availability").text.strip()

                image_url = book.find("img")["src"]
                image_url = urljoin(self.url,image_url)
                product_url = book.h3.a["href"]
                books.append(Book(title, price,rating,availability,image_url,product_url))
            
        return books

    def save_to_csv(self, books):

        with open(
            "data/raw/books_raw.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Title",
                "Price",
                "Rating",
                "Availability",
                "Image URL",
                "Product URL"
            ])

            for book in books:

                writer.writerow([
                    book.title,
                    book.price,
                    book.rating,
                    book.availability,
                    book.image_url,
                    book.product_url
                ])

        print("✅ Books saved successfully!")