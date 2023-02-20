import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.demoblaze.com/")
try:
    driver.find_element(By.XPATH, '//a[@class="nav-link"][@href="index.html"]')
    print("Home element is located")
except NoSuchElementException:
    print("No Such Element")
try:
    driver.find_element(By.XPATH,'//a[@class="nav-link"][@data-target="#exampleModal"]')
    print("Contact element is located")
except NoSuchElementException:
    print("No Such Element")

try:
    driver.find_element(By.XPATH,'//a[@class="nav-link"][@data-target="#videoModal"]')
    print("About us element is located")
except NoSuchElementException:
    print("No Such Element")

try:
    driver.find_element(By.XPATH,'//a[@id="cartur"]')
    print("Cart element is located")
except NoSuchElementException:
    print("No Such Element")

try:
    driver.find_element(By.XPATH,"//a[@id='login2']")
    print("Login element is located")
except NoSuchElementException:
    print("No Such Element")

try:
    driver.find_element(By.XPATH,'//a[@id="signin2"]')
    print("Sign up element is located")
except NoSuchElementException:
    print("No Such Element")
time.sleep(5)

driver.quit()



