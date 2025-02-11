from .pages.product_page import ProductPage
import time


# Проверка ссылки авторизации
def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_save_product_name()
    page.find_and_save_product_price()
    page.add_product_to_basket()
    page.is_product_name_in_basket_present()
    page.compare_product_name()
    page.is_product_price_in_basket_present()
    page.compare_product_price()

