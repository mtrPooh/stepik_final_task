from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time


# Проверка ссылки авторизации
def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    time.sleep(10)


# Проверка перехода на страницу авторизации
def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
