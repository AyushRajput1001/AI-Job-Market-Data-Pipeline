from scraper.book_scraper import BookScraper

def test_fetch_page():
    scraper = BookScraper()

    soup = scraper.fetch_page(scraper.BASE_URL.format(1))

    assert soup is not None