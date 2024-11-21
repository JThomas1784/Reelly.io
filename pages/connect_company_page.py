class ConnectCompanyPage:
    def __init__(self, driver):
        self.driver = driver

    def is_correct_page_open(self):
        """Verifies that the correct page opened by checking the URL."""
        expected_url = "https://soft.reelly.io/expected_page_after_connect"  # Replace with actual URL
        return self.driver.current_url == expected_url
