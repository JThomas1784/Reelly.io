from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def before_all(context):
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    context.driver = webdriver.Firefox(options=firefox_options)
    context.browser.maximize_window()

# def before_all(context):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     context.browser = webdriver.Chrome(options=chrome_options)
#     context.browser.maximize_window()

def after_all(context):
    context.browser.quit()