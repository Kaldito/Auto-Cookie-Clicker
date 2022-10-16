import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()


def select_lgn():
    time.sleep(5)
    language = driver.find_element(By.XPATH, '//*[@id="langSelect-ES"]')
    language.click()


def start_game():
    time.sleep(5)
    btn_dismiss = driver.find_element(By.LINK_TEXT, "Got it!")
    btn_dismiss.click()

    big_cookie = driver.find_element(By.ID, "bigCookie")

    timeout = time.time() + 60 * 5
    clicks = 400

    while True:
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test -= 1

        for i in range(0, clicks):
            big_cookie.click()

        upgrades_table = driver.find_element(By.ID, "upgrades")
        upgrades = upgrades_table.find_elements(By.CSS_SELECTOR, ".upgrade")
        for upgrade in upgrades:
            try:
                upgrade.click()
            except StaleElementReferenceException:
                pass

        products_table = driver.find_element(By.ID, "products")
        products = products_table.find_elements(By.CSS_SELECTOR, ".unlocked")
        products.reverse()

        for product in products:
            product.click()

        try:
            golden_cookie = driver.find_element(By.CSS_SELECTOR, "shimmer")
            golden_cookie.click()
        except NoSuchElementException:
            pass

        clicks += 15


select_lgn()
start_game()




