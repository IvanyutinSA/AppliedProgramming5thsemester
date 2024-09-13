from playwright.sync_api import expect

from pages.login_po import LoginPage


def test_blank_login(page):
    username = ""
    password = ""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    expect(login_page.error_locator).to_have_text(
            "Epic sadface: Username is required")
