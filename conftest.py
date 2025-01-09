import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Опции командной строки.
        В командную строку передается параметр вида '--language=ru'
        """
    parser.addoption('--language', action='store', default='en',
                     help="Set language: ru, en, de etc.")

@pytest.fixture(scope="function")
def browser(request):
    # В переменную language передается параметр из командной строки
    language = request.config.getoption("language")

    print("\nstart chrome browser for test..")

    # Инициализируются опции браузера
    options = Options()

    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

