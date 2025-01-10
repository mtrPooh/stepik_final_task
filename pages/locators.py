from selenium.webdriver.common.by import By


class MainPageLocators():
    # Ссылка авторизации
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # Форма авторизации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    # Форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
