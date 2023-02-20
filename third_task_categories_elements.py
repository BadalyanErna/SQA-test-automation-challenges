import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.demoblaze.com/")

try:
    driver.find_element(By.CSS_SELECTOR, '#itemc[onclick="byCat(\'phone\')"]').click()
    print("Element is located")
except NoSuchElementException:
    print("No Such Element")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'img.card-img-top[src="imgs/Lumia_1520.jpg"]').click()
time.sleep(3)
driver.back()
try:
    driver.find_element(By.CSS_SELECTOR, '#itemc[onclick="byCat(\'notebook\')"]').click()
    print("Element is located")
except NoSuchElementException:
    print("No Such Element")
time.sleep(3)
el = driver.find_elements(By.CSS_SELECTOR, 'img.img-fluid[src="imgs/macbook_air.jpg"]')
el[1].click()
driver.back()
try:
    driver.find_element(By.CSS_SELECTOR, '#itemc[onclick="byCat(\'monitor\')"]').click()
    print("Element is located")
except NoSuchElementException:
    print("No Such Element")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'img.img-fluid[src="imgs/apple_cinema.jpg"]').click()
time.sleep(4)

driver.quit()
