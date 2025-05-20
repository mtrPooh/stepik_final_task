from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


# Проверка добавления товара в корзину
@pytest.mark.parametrize('offer_num', ["0", "1", "2", "3", "4", "5", "6",
                                       pytest.param("bugged_offer_num", marks=pytest.mark.xfail),
                                       "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_save_product_name()
    page.find_and_save_product_price()
    page.add_product_to_basket()
    page.is_product_name_in_basket_present()
    page.compare_product_name()
    page.is_product_price_in_basket_present()
    page.compare_product_price()

# Проверка отсутствия уведомлений после добавления товара в корзину
@pytest.mark.xfail(reason="Excpected fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

# Проверка отсутствия уведомлений при переходе на страницу товара
def test_guest_cant_see_success_message(browser):
    link = f"https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# Проверка исчезновения уведомлений после добавления товара в корзину
@pytest.mark.xfail(reason="Excpected fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_of_success_message()

# Проверка наличия ссылки на страницу авторизации на странице товара
def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# Проверка перехода на страницу авторизации со страницы товара
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

