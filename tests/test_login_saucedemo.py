from playwright.sync_api import expect

def test_login_saucedemo(login_page):
    login_page.open()

    expect(login_page.page).to_have_title("Swag Labs")
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()
    
