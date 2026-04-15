from pages.google_search_page import GoogleSearchPage

def test_google_search(page, base_url):
    google_page = GoogleSearchPage(page)
    google_page.navigate(base_url)
    google_page.search("Playwright Python")
    assert "Playwright Python" in page.title()

def test_google_lucky_search(page, base_url):
    google_page = GoogleSearchPage(page)
    google_page.navigate(base_url)
    google_page.lucky_search("Playwright")
    assert "Playwright" in page.title()