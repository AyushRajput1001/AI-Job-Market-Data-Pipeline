import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

with open("data/raw/books_raw.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Title", "Price"])

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        writer.writerow([title, price])

print("Books saved successfully!")
