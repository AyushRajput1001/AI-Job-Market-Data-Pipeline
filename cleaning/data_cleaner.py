import pandas as pd

class DataCleaner:

    def __init__(self):
        self.input_file = ("data/raw/books_raw.csv")
        self.output_file = ("data/cleaned/books_cleaned.csv")

    def load_data(self):
        df = pd.read_csv(self.input_file)
        return df
    
    def clean_data(self,df):

        # remove duplicates rows
        df = df.drop_duplicates()

        # Remove rows with missing values
        df = df.dropna()
        def price_category(price):
            if price < 20:
                return "Cheap"
            elif price < 40:
                return "Medium"
            else:
                return "Expensive"

        df["Price Category"] = df["Price"].apply(price_category)
        # Remove leading and trailing spaces from text columns
        df["Title"] = df["Title"].str.strip()
        df["Availability"] = df["Availability"].str.strip()

        return df

    def save_clean_data(self, df):
        df.to_csv(self.output_file, index=False)
        print("✅ Cleaned data saved successfully!")
