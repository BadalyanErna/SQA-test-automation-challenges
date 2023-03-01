from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from waits import Wait
from waits import get_driver

driver = webdriver.Chrome()


class Tests:

    def test_first_task_open_website_one_edge_and_firefox(self):
        edge_driver = get_driver('Edge')
        firefox_driver = get_driver('Firefox')
        edge_driver.get('https://www.demoblaze.com/')
        # firefox_driver.get('https://www.demoblaze.com/')
        firefox_driver.close()

    def test_second_task_locate_elements_on_webpage(self):
        global driver
        get_wait = Wait(driver)
        driver.get("https://www.demoblaze.com/")

        try:
            get_wait.wait_for_element(By.XPATH, '//a[@class="nav-link"][@href="index.html"]')
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

    def test_third_task_categories_elements(self):
        global driver
        get_wait = Wait(driver)
        try:
            get_wait.wait_for_element(By.CSS_SELECTOR, '#itemc[onclick="byCat(\'phone\')"]')
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

    def test_categories_section(self):

        global driver
        get_wait = Wait(driver)
        phones = get_wait.wait_for_element(By.XPATH, '//a[@onclick="byCat(\'phone\')"]')
        phones.click()
        assert get_wait.wait_for_element(By.XPATH, '//div[@id="tbodyid"]').is_displayed()

        laptops = driver.find_element(By.XPATH, '//a[@onclick="byCat(\'notebook\')"]')
        laptops.click()
        assert get_wait.wait_for_element(By.XPATH, '//div[@id="tbodyid"]').is_displayed()

        monitors = driver.find_element(By.XPATH, '//a[@onclick="byCat(\'monitor\')"]')
        monitors.click()
        assert get_wait.wait_for_element(By.XPATH, '//div[@id="tbodyid"]').is_displayed()
