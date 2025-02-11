from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class BasePage():

    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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

    # Проверка кликабельности элемента на странице
    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((how, what))
            )
        except (TimeoutException):
            return False
        return True

