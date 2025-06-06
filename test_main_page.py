from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Проверка ссылки авторизации
    def test_guest_should_see_login_link(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()


    # Проверка перехода на страницу авторизации
    def test_guest_can_go_to_login_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

# Проверка отсутствия товаров в корзине при переходе в корзину с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.no_products_in_basket()
    basket_page.basket_is_empty_message_exists()


