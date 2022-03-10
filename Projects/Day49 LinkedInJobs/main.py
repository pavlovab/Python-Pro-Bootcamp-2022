from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

MY_EMAIL = [YOUR_EMAIL]
MY_PASSWORD = [YOUR_PASSWORD]

chrome_driver_path = [YOUR_CHROME_DRIVER_PATH]
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(MY_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(MY_PASSWORD)
password_field.send_keys(Keys.ENTER)


all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()