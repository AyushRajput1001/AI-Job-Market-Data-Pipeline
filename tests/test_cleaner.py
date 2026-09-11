import pandas as pd
from cleaning.data_cleaner import DataCleaner


def test_clean_data():
    cleaner = DataCleaner()

    df = pd.DataFrame({
        "Title": ["Book A", "Book B"],
        "Price": [20.5, 30.0],
        "Rating": [4, 5],
        "Availability": ["In stock", "In stock"],
        "Image URL": ["img1", "img2"],
        "Product URL": ["url1", "url2"]
    })

    cleaned_df = cleaner.clean_data(df)

    assert len(cleaned_df) == 2