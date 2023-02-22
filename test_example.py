import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from waits import Wait

driver = webdriver.Chrome()


def browser_navigation():
    # Keep drivers in PATH
    global driver
    driver.get("https://www.demoblaze.com/")



class Tests:

    def second_task_locate_elements_on_webpage(self):
        global driver
        driver.get("https://www.demoblaze.com/")
        self.get_wait = Wait(driver)

        try:
            self.get_wait.wait_for_element(By.XPATH, '//a[@class="nav-link"][@href="index.html"]')
            print("Home element is located")
        except NoSuchElementException:
            print("No Such Element")
        try:
            driver.find_element(By.XPATH, '//a[@class="nav-link"][@data-target="#exampleModal"]')
            print("Contact element is located")
        except NoSuchElementException:
            print("No Such Element")

        try:
            driver.find_element(By.XPATH, '//a[@class="nav-link"][@data-target="#videoModal"]')
            print("About us element is located")
        except NoSuchElementException:
            print("No Such Element")

        try:
            driver.find_element(By.XPATH, '//a[@id="cartur"]')
            print("Cart element is located")
        except NoSuchElementException:
            print("No Such Element")

        try:
            driver.find_element(By.XPATH, "//a[@id='login2']")
            print("Login element is located")
        except NoSuchElementException:
            print("No Such Element")

        try:
            driver.find_element(By.XPATH, '//a[@id="signin2"]')
            print("Sign up element is located")
        except NoSuchElementException:
            print("No Such Element")

    def third_task_categories_elements(self):
        global driver
        try:
            self.get_wait.wait_for_element(By.XPATH, '#itemc[onclick="byCat(\'phone\')"]')
            print("Element is located")
        except NoSuchElementException:
            print("No Such Element")
        try:
            driver.find_element(By.CSS_SELECTOR, '#itemc[onclick="byCat(\'notebook\')"]')
            print("Element is located")
        except NoSuchElementException:
            print("No Such Element")
        try:
            driver.find_element(By.CSS_SELECTOR, '#itemc[onclick="byCat(\'monitor\')"]').click()
            print("Element is located")
        except NoSuchElementException:
            print("No Such Element")

    def fourth_task_highest_price_phone(self):
        global driver
        phones = self.get_wait.wait_for_element(By.XPATH, '//a[@onclick="byCat(\'phone\')"]')
        phones.click()
        self.get_wait.wait_for_element(By.XPATH, '//div[@class="card h-100"]')
        phones_name_and_price = {}

        # iterating over the list of phones and extracting their name and price
        for phone in phones:
            nameElements = phone.find_element(By.CLASS_NAME, 'hrefch')
            name = nameElements.text
            priceElement = phone.find_element(By.TAG_NAME, "h5")
            price = int(priceElement.text[1:])
            phones_name_and_price[name] = price
        print(phones_name_and_price)

        # defining a function to get phone's price using its name
        def get_price_of_phone(phone_name):
            return phones_name_and_price[phone_name]

        # finding the phone with the highest price
        max_key = max(phones_name_and_price, key=get_price_of_phone)
        max_value = phones_name_and_price[max_key]
        print(f"The highest phone is {max_key} and the price is ${max_value}")

    def test_categories_section(self):
        global driver
        phones = self.get_wait.wait_for_element(By.XPATH, '//a[@onclick="byCat(\'phone\')"]')
        phones.click()
        assert self.get_wait.wait_for_element(By.XPATH, '//div[@id="tbodyid"]').is_displayed()

        laptops = self.get_wait.wait_for_el
