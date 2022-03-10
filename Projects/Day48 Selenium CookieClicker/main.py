# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = [YOUR_CHROME_DRIVER_PATH]
driver = webdriver.Chrome(chrome_driver_path)


driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

def clicker():
    check_timer = time.time() + 5
    while time.time() < check_timer:
        cookie.click()
    check()

def check():
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    items.reverse()
    for item in items:
        if item.get_attribute('class') != "grayed":
            item.click()
            break

    if time.time() < timeout:
        clicker()


timeout = time.time() + 60 * 5

cookies_per_sec = driver.find_element(By.ID, "cps")
clicker()

print(cookies_per_sec.text)

driver.quit()