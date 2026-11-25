import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru",
                     help="Choose interface language: ru, en, es, ...")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    print("\nStart chrome browser...")
    options = ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()
