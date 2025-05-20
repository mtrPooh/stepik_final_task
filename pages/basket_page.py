from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # Проверка отсутствия товаров в корзине
    def no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "Products should not present in basket"

    # Проверка наличия сообщения о пустой корзине
    def basket_is_empty_message_exists(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket empty message not found"

