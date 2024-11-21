from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    LOGIN_BUTTON = (By.ID, "//*[@id="wf-form-Sign-up"]/a")
    CONNECT_COMPANY_BUTTON = (By.ID, "//*[@id="w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b"]/div[2]/a/div")  # Adjust the locator

    def login(self, username, password):
        self.browser.find_element(By.ID, "//*[@id="email-2"]").send_keys(username)
        self.browser.find_element(By.ID, "//*[@id="field"]").send_keys(password)
        self.click_element(self.LOGIN_BUTTON)

    def click_connect_company(self):
        self.click_element(self.CONNECT_COMPANY_BUTTON)
