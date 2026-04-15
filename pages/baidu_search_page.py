from pages.base_page import BasePage

class BaiduSearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = "#kw"
        self.search_button = "#su"
        self.news_link = "#s-top-left > a:nth-child(1)"
        self.hao123_link = "#s-top-left > a:nth-child(2)"
        self.map_link = "#s-top-left > a:nth-child(3)"
        self.video_link = "#s-top-left > a:nth-child(4)"
        self.images_link = "#s-top-left > a:nth-child(5)"
    
    def search(self, keyword: str):
        self.fill(self.search_input, keyword)
        self.click(self.search_button)
    
    def go_to_news(self):
        self.click(self.news_link)
    
    def go_to_hao123(self):
        self.click(self.hao123_link)
    
    def go_to_map(self):
        self.click(self.map_link)
    
    def go_to_video(self):
        self.click(self.video_link)
    
    def go_to_images(self):
        self.click(self.images_link)