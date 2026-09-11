import pandas as pd


class FeatureEngineer:

    def add_title_length(self, df):

        df["Title Length"] = df["Title"].apply(len)

        return df
    def add_price_category(self, df):

        def category(price):

            if price < 20:
                return "Cheap"

            elif price < 40:
                return "Medium"

            else:
                return "Expensive"

        df["Price Category"] = df["Price"].apply(category)

        return df