from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from waits import Wait


class Tests:

    def test_radiobutton(self, driver):
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

    def test_checkboxes(self, driver):
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

    def test_dropdown(self, driver):
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        cars = get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)
        cars_select.select_by_value('honda')
        assert cars_select.first_selected_option.is_selected()

    def test_multi_select(self, driver):
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        fruits = get_wait.wait_for_element(By.ID, "multiple-select-example")
        fruits_select = Select(fruits)
        fruits_select.select_by_value('apple')
        fruits_select.select_by_value('peach')
        for fruit in fruits_select.all_selected_options:
            assert 'orange' not in fruits_select.all_selected_options

    def test_enabled_disabled_placeholder(self, driver):
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        enabled_button = get_wait.wait_for_element(By.CSS_SELECTOR, 'input#enabled-button')
        enabled_button.click()
        assert enabled_button.is_enabled()

        driver.find_element(By.CSS_SELECTOR, "input#enabled-example-input").send_keys('Hello')
        disabled = driver.find_element(By.CSS_SELECTOR, 'input#disabled-button')
        disabled.click()
        disabled_placeholder_element = driver.find_element(By.CSS_SELECTOR,
                                                           'input[placeholder="Enabled/Disabled Field"][disabled]')
        assert not disabled_placeholder_element.is_enabled()

    def test_hover_reload(self, driver):
        driver = webdriver.Chrome()
        get_wait = Wait(driver)
        driver.get('https://courses.letskodeit.com/practice')
        fruits = get_wait.wait_for_element(By.ID, "multiple-select-example")
        fruits_select = Select(fruits)
        fruits_select.select_by_value('apple')
        fruits_select.select_by_value('peach')
        mouse_hover = get_wait.wait_for_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        actions = ActionChains(driver)
        actions.move_to_element(mouse_hover).perform()
        driver.find_element(By.ID, "multiple-select-example").click()
        assert not fruits_select.select_by_value('apple')
        assert not fruits_select.select_by_value('peach')
