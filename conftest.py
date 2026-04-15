import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    # 无头模式启动，适配Jenkins服务器
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    # 新建页面，不依赖错误的base_url
    page = browser.new_page()
    # 设置全局超时，避免30s超时
    page.set_default_timeout(15000)
    yield page
    page.close()

# 覆盖base_url fixture，强制百度用例走正确网址
@pytest.fixture(scope="session")
def base_url():
    return "https://www.baidu.com"
