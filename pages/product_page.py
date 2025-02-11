from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math


class ProductPage(BasePage):

    product_name = ''
    product_price = ''

    # Поиск и сохранение названия товара (чтобы затем сравнить с названием товара в корзине)
    def find_and_save_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name not found"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.product_name = product_name.text

    # Поиск и сохранение цены товара (чтобы затем сравнить с ценой товара в корзине)
    def find_and_save_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price not found"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.product_price = product_price.text

    # Добавление товара в корзину
    def add_product_to_basket(self):
        assert self.is_element_clickable(*ProductPageLocators.BASKET_BUTTON), "Basket button is not clickable"
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code(), "Can't solve the quiz"

    # Проверка наличия названия товара в корзине
    def is_product_name_in_basket_present(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "Product name in basket not found"

    # Сравнение названия товара в корзине
    def compare_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name.text == self.product_name, "Product name is not equal"

    # Проверка наличия цены товара в корзине
    def is_product_price_in_basket_present(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE_IN_BASKET), "Product price in basket not found"

    # Сравнение цены товара в корзине
    def compare_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price.text == self.product_price, "Product price is not equal"

    # Получение проверочного кода
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except TimeoutException:
            print("No second alert presented")

