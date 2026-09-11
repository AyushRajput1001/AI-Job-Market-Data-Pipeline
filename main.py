from scraper.book_scraper import BookScraper
from cleaning.data_cleaner import DataCleaner
from analytics.eda import BookEDA
from feature_engineering.feature_engineer import FeatureEngineer
from analytics.visualizer import Visualizer
from database.database import Base, engine
from database.models import BookDB

Base.metadata.create_all(bind=engine)

# scrape data
# scraper = BookScraper()
# books = scraper.scrape()
# scraper.save_to_csv(books)


# for book in books:
#     print(book)

# print(len(books))

# load raw csv
cleaner = DataCleaner()

df = cleaner.load_data()
clean_df = cleaner.clean_data(df)

cleaner.save_clean_data(clean_df)

print(clean_df.head())
print(df.head())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nDescribe")
print(df.describe())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nMissing Values")
print(df.isnull().sum())

eda = BookEDA(clean_df)

eda.overview()

eda.statistics()

eda.highest_price()

eda.lowest_price()

eda.average_price()

eda.average_rating()

eda.expensive_book()

eda.cheapest_book()

eda.rating_counts()

eda.availability()

print(clean_df.head())

print(clean_df["Price Category"].value_counts())

print(clean_df.groupby("Price Category")["Price"].mean())

engineer = FeatureEngineer()

df = engineer.add_title_length(df)

print(df.head())

visualizer = Visualizer()

visualizer.plot_rating_distribution(clean_df)
visualizer.plot_price_distribution(clean_df)
visualizer.plot_average_price_by_rating(clean_df)
visualizer.plot_rating_pie(clean_df)

from database.database_manager import DatabaseManager

db = DatabaseManager()

connection = db.connect()

print(connection)
connection.close()

print("Connection Closed")

from database.database_manager import DatabaseManager

db = DatabaseManager()

db.create_table()

from database.database_manager import DatabaseManager

db = DatabaseManager()

db.create_table()

db.insert_books(clean_df)


from analytics.analyzer import BookAnalyzer

analyzer = BookAnalyzer()

print(analyzer.average_price())

print(analyzer.total_books())

print(analyzer.average_price())

print(analyzer.five_star_books().head())


print(analyzer.expensive_books().head())

print(analyzer.books_by_rating())

print(analyzer.average_price_by_rating())

print(analyzer.top_expensive_books())

print(analyzer.cheapest_books())

print(analyzer.available_books())

print(analyzer.highest_rated_books().head())

print(analyzer.books_above_average_price())

print(analyzer.books_below_average_price())