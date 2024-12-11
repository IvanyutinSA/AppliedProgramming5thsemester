class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_jacket_locator = page.locator(
                "[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def add_jacket(self):
        self.add_to_cart_jacket_locator.click()
