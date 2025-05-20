from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    # Переход на страницу авторизации
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Проверка наличия ссылки авторизации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Переход по ссылке
    def open(self):
        self.browser.get(self.url)

    # Проверка наличия элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Проверка отсутствия элемента на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Проверка исчезновения элемента на странице
    def is_elemenent_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Проверка кликабельности элемента на странице
    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((how, what))
            )
        except (TimeoutException):
            return False
        return True

