from playwright.sync_api import expect

from pages.login_po import LoginPage
from pages.products_po import ProductsPage
from pages.cart_po import CartPage
from pages.checkout_po import CheckoutPage


def test_placing_an_order_with_correct_data(page):
    username = "standard_user"
    password = "secret_sauce"
    first_name = "Cris"
    last_name = "Motionless"
    postal_code = "570"

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()
    login_page.login(username, password)

    products_page.navigate()
    products_page.add_jacket()

    cart_page.navigate()
    cart_page.checkout()

    checkout_page.navigate()
    checkout_page.fill_information(first_name, last_name, postal_code)
    checkout_page.finish()

    expect(checkout_page.is_complete_title_exist()).to_have_text(
            "Thank you for your order!")
