class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator(
                "[data-test=\"firstName\"]"
                )
        self.last_name = page.locator(
                "[data-test=\"lastName\"]"
                )
        self.postal_code = page.locator(
                "[data-test=\"postalCode\"]"
                )
        self.to_continue = page.locator(
                "[data-test=\"continue\"]"
                )
        self.to_finish = page.locator(
                "[data-test=\"finish\"]"
                )
        self.complete_title = page.locator(
                "[data-test=\"complete-header\"]"
                )

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/checkout-step-one.html")

    def fill_information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.to_continue.click()

    def finish(self):
        self.to_finish.click()

    def is_complete_title_exist(self):
        return self.complete_title
