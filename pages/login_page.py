from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    # Проверка страницы авторизации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка корректности URL
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Page URL is not login URL"

    # Проверка наличия формы авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # Проверка наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    # Регистрация нового пользователя
    def register_new_user(self, email, password):
        self.go_to_login_page()
        try:
            el = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            el.send_keys(email)
            el = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
            el.send_keys(password)
            el = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
            el.send_keys(password)
            el = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
            el.click()
        except (NoSuchElementException):
            return False
