import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)