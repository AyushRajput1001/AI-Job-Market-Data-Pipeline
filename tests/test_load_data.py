from cleaning.data_cleaner import DataCleaner

def test_load_data():
    cleaner = DataCleaner()

    df = cleaner.load_data()

    assert not df.empty