from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.XPATH, //*[@id="email-2"])
        self.password_field = (By.XPATH, //*[@id="field"])
        self.login_button = (By.XPATH, "//button[text()='Continue']")

    def login(self, username, password):
        """Logs into the application with the given credentials."""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
