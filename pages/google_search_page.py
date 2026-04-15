from pages.base_page import BasePage

class GoogleSearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = "#APjFqb"
        self.search_button = "input[value='Google 搜索']"
        self.lucky_button = "input[value='我 Feeling Lucky']"
    
    def search(self, keyword: str):
        self.fill(self.search_input, keyword)
        self.click(self.search_button)
    
    def lucky_search(self, keyword: str):
        self.fill(self.search_input, keyword)
        self.click(self.lucky_button)