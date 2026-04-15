from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        self.page.goto(url)
    
    def click(self, locator: str):
        self.page.click(locator)
    
    def fill(self, locator: str, text: str):
        self.page.fill(locator, text)
    
    def get_text(self, locator: str) -> str:
        return self.page.text_content(locator)
    
    def wait_for_selector(self, locator: str, timeout: int = 30000):
        self.page.wait_for_selector(locator, timeout=timeout)
    
    def is_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)
    
    def get_title(self) -> str:
        return self.page.title()
    
    def take_screenshot(self, path: str):
        self.page.screenshot(path=path)