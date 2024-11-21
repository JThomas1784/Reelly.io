from pages.main_page import MainPage

class Application:
    def __init__(self, browser):
        self.main_page = MainPage(browser)