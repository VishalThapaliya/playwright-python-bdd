from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect

# Given section
@given("I open the SauceDemo login page")
def open_login_page(login_page):
    login_page.open()


#  When section
@when(parsers.parse('I log in with username "{username}" and password "{password}"'))
def login_with_valid_credentials(login_page, username, password):
    login_page.login(username, password)


#  Then section
@then('the login page title should be "Swag Labs"')
def verify_login_page_title(login_page):
    expect(login_page.page).to_have_title("Swag Labs")

@then("the username field should be visible")
def verify_username_field(login_page):
    expect(login_page.username_input).to_be_visible()

@then("the password field should be visible")
def verify_password_field(login_page):
    expect(login_page.password_input).to_be_visible()

@then("the login button should be visible")
def verify_login_button(login_page):
    expect(login_page.login_button).to_be_visible()

@then("I should be on the poducts page")
def verify_products_page(products_page):
    expect(products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")