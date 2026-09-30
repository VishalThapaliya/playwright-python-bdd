def test_saucedemo_is_available(page):
    page.goto("https://www.saucedemo.com/")

    assert page.title() == "Swag Labs"