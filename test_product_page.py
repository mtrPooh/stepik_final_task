from .pages.product_page import ProductPage
import pytest
import time


# Проверка добавления товара в корзину
@pytest.mark.parametrize('offer_num', ["0", "1", "2", "3", "4", "5", "6",
                                       pytest.param("bugged_offer_num", marks=pytest.mark.xfail),
                                       "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.find_and_save_product_name()
    page.find_and_save_product_price()
    page.add_product_to_basket()
    page.is_product_name_in_basket_present()
    page.compare_product_name()
    page.is_product_price_in_basket_present()
    page.compare_product_price()

