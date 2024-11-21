class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def click_element(self, locator):
        element = self.browser.find_element(*locator)
        element.click()

    def switch_to_new_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def get_current_url(self):
        return self.browser.current_url