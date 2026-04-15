from pages.baidu_search_page import BaiduSearchPage
from playwright.sync_api import expect

def test_baidu_search(page):
    """百度搜索真实用例（国内可跑）"""
    baidu_page = BaiduSearchPage(page)
    # 直接指定百度网址，不依赖错误的base_url
    baidu_page.navigate("https://www.baidu.com")
    # 加显式等待，避免超时
    page.wait_for_selector("#kw", timeout=10000)
    baidu_page.search("Playwright Python")
    # 验证搜索结果
    expect(page).to_have_title("Playwright Python_百度搜索")

def test_baidu_news_link(page):
    """百度新闻链接真实用例（国内可跑）"""
    baidu_page = BaiduSearchPage(page)
    baidu_page.navigate("https://www.baidu.com")
    page.wait_for_selector("#s-top-left > a:nth-child(1)", timeout=10000)
    baidu_page.go_to_news()
    expect(page).to_have_title("百度新闻——海量中文资讯平台")

def test_baidu_hao123_link(page):
    """百度hao123链接真实用例（国内可跑）"""
    baidu_page = BaiduSearchPage(page)
    baidu_page.navigate("https://www.baidu.com")
    page.wait_for_selector("#s-top-left > a:nth-child(2)", timeout=10000)
    baidu_page.go_to_hao123()
    expect(page).to_have_title("hao123_上网从这里开始")
