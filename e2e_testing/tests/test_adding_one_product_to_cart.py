from playwright.sync_api import expect

from pages.login_po import LoginPage
from pages.products_po import ProductsPage
from pages.cart_po import CartPage


def test_adding_one_product_to_cart(page):
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login(username, password)

    products_page.navigate()
    products_page.add_jacket()

    cart_page.navigate()

    expect(cart_page.amount_of_products()).to_have_text("1")
    expect(cart_page.jacket_exist()).to_be_visible()
