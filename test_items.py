from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_is_displayed(browser):
    browser.get(link)
    # Раскомментируйте строку ниже для визуальной проверки языка
    # time.sleep(30)
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button.is_displayed(), "basket button is not displayed"
