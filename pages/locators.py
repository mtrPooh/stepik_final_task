from selenium.webdriver.common.by import By


class MainPageLocators():
    # Ссылка авторизации
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # Форма авторизации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    # Форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    # Название товара
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")

    # Цена товара
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']")

    # Кнопка добавления в корзину
    BASKET_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button[contains(@class, 'btn-add-to-basket')]")

    # Название товара в корзине
    PRODUCT_NAME_IN_BASKET = (
        By.XPATH,
        "//div[@id='messages']/div[contains(@class, 'alert-success')]/div[contains(@class, 'alertinner')]/strong"
    )

    # Цена товара в корзине
    PRODUCT_PRICE_IN_BASKET = (
        By.XPATH,
        "//div[@id='messages']/div[contains(@class, 'alert-info')]/div[contains(@class, 'alertinner')]/p/strong"
    )

