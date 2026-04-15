from pages.baidu_search_page import BaiduSearchPage

def test_baidu_search(page, base_url):
    baidu_page = BaiduSearchPage(page)
    baidu_page.navigate(base_url)
    baidu_page.search("Playwright Python")
    assert "Playwright Python" in page.title()

def test_baidu_news_link(page, base_url):
    baidu_page = BaiduSearchPage(page)
    baidu_page.navigate(base_url)
    baidu_page.go_to_news()
    assert "百度新闻" in page.title()

def test_baidu_hao123_link(page, base_url):
    baidu_page = BaiduSearchPage(page)
    baidu_page.navigate(base_url)
    baidu_page.go_to_hao123()
    assert "hao123" in page.title()