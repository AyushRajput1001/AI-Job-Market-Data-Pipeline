import matplotlib.pyplot as plt

class Visualizer:

    def plot_rating_distribution(self, df):

        rating_counts = df["Rating"].value_counts().sort_index()

        plt.figure(figsize=(8,5))

        plt.bar(rating_counts.index, rating_counts.values)

        plt.title("Book Ratings")

        plt.xlabel("Rating")

        plt.ylabel("Number of Books")

        plt.show()
    
    def plot_price_distribution(self, df):

        plt.figure(figsize=(8,5))

        plt.hist(df["Price"], bins=10)

        plt.title("Price Distribution")

        plt.xlabel("Price (£)")

        plt.ylabel("Number of Books")

        plt.show()
    
    def plot_average_price_by_rating(self, df):

        average = df.groupby("Rating")["Price"].mean()

        plt.figure(figsize=(8,5))

        plt.bar(average.index, average.values)

        plt.title("Average Price by Rating")

        plt.xlabel("Rating")

        plt.ylabel("Average Price (£)")

        plt.show()

    def plot_rating_pie(self, df):

        ratings = df["Rating"].value_counts()

        plt.figure(figsize=(7,7))

        plt.pie(
            ratings.values,
            labels=ratings.index,
            autopct="%1.1f%%"
        )

        plt.title("Ratings Percentage")

        plt.show()

    def plot_price_boxplot(self, df):

        plt.figure(figsize=(6,4))

        plt.boxplot(df["Price"])

        plt.title("Price Box Plot")

        plt.ylabel("Price")

        plt.show()

    def plot_price_vs_rating(self, df):

        plt.figure(figsize=(7,5))

        plt.scatter(df["Rating"], df["Price"])

        plt.xlabel("Rating")

        plt.ylabel("Price")

        plt.title("Price vs Rating")

        plt.show()