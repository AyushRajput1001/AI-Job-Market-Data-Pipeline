import pandas as pd

class BookEDA:
    def __init__(self,df):
        self.df = df

    def overview(self):

        print("Rows:", self.df.shape[0])
        print("Columns:", self.df.shape[1])

        print("\nColumn Names")

        print(self.df.columns)

    def statistics(self):

        print(self.df.describe())

    def highest_price(self):

        print(self.df["Price"].max())

    def lowest_price(self):

        print(self.df["Price"].min())

    def average_price(self):

        print(self.df["Price"].mean())
    
    def average_rating(self):

        print(self.df["Rating"].mean())

    def expensive_book(self):

        print(self.df.loc[self.df["Price"].idxmax()])

    def cheapest_book(self):

        print(self.df.loc[self.df["Price"].idxmin()])
    
    def rating_counts(self):

        print(self.df["Rating"].value_counts())

    def availability(self):

        print(self.df["Availability"].value_counts())