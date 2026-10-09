from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def is_open(self):
        return self.page.url.endswith('/inventory.html')