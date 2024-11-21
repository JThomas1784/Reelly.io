from behave import given, when, then
from app.application import Application

@given("I am on the main page")
def step_open_main_page(context):
    context.app = Application(context.browser)
    context.app.main_page.navigate_to("https://soft.reelly.io")

@given("I log in with valid credentials")
def step_login(context):
    context.app.main_page.login(username="jamonte.thomas17@gmail.com", password="9#p9PW6bLVCF8gt")

@when("I click \"Connect the company\"")
def step_click_connect_company(context):
    context.app.main_page.click_connect_company()

@then("I should see the correct new tab opened")
def step_verify_new_tab(context):
    context.app.main_page.switch_to_new_tab()
    expected_url = "https://soft.reelly.io/payment/personal"
    assert expected_url in context.app.main_page.get_current_url(), "New tab URL is incorrect."