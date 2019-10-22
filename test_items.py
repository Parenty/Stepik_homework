from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_purchase_button(browser):
    browser.get(link)
    # Пожалуйста, убедитесь что у вас в директориях выше нет файла conftest.py
    # Согласно заданию запускайте код так: pytest --language=es
    # Проверяющим: Если хотите проверить смену языка - раскоментируйте следующую строчку
    # time.sleep(30)
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        assert True, "Нет кнопки 'добавить в корзину' "
    except NoSuchElementException:
        assert False, "Нет кнопки 'добавить в корзину' "
