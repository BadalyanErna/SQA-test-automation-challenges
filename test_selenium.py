from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from waits import Wait
import pytest

driver = webdriver.Chrome()


class Tests:

    def test_radiobutton(self):
        global driver
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        benz_radiobutton = get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="benzradio"]')
        benz_radiobutton.click()
        bmv_radiobutton = driver.find_element(By.CSS_SELECTOR, 'input[id="bmwradio"]')
        honda_radiobutton = driver.find_element(By.CSS_SELECTOR, 'input[id="hondaradio"]')
        assert benz_radiobutton.is_selected()
        assert not bmv_radiobutton.is_selected()
        assert not honda_radiobutton.is_selected()

    def test_checkboxes(self):
        global driver
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        bmw_checkbox = get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="bmwcheck"]')
        bmw_checkbox.click()
        benz_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[id="benzcheck"]')
        honda_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[id="hondacheck"]')
        assert not honda_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert bmw_checkbox.is_selected()

    def test_dropdown(self):
        global driver
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        cars = get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)
        cars_select.select_by_value('honda')
        assert cars_select.first_selected_option.is_selected()

    def test_hover_reload(self):
        global driver
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        mouse_hover = get_wait.wait_for_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        actions = ActionChains(driver)
        actions.move_to_element(mouse_hover).perform()
        driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[2]").click()
        cars = get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)
        assert cars_select.first_selected_option.is_selected()



