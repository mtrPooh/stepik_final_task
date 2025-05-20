from selenium.webdriver.common.by import By


class BasePageLocators():
    # Ссылка авторизации
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    # Невалидная ссылка авторизации
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    # Иконка авторизованного пользователя
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    # Форма авторизации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    # Форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # Поле ввода емеил для регистрации
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")

    # Поле ввода пароля для регистрации
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")

    # Поле ввода подтверждения пароля для регистрации
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")

    # Кнопка регистрации
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


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

    # Сообщение об успешном добавлении товара в корзину
    PRODUCT_ADDED_SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[@id='messages']/div[contains(@class, 'alert-success')]/div[contains(@class, 'alertinner')]/strong"
    )


class BasketPageLocators():
    # Кнопка перехода в корзину
    BASKET_BUTTON = (By.XPATH, "//div[contains(@class, 'basket-mini')]//a")

    # Товары в корзине
    BASKET_PRODUCTS = (By.XPATH, "//div[@id='content_inner']//div[@class='row']//p")

    # Сообщение о пустой корзине
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")

