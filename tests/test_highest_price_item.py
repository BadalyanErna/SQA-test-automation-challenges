from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test:

    def test_find_highest_price_item(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        # navigating to the main page
        driver.get("https://www.demoblaze.com/")

        # locating the products elements from the first page
        products = driver.find_elements(By.ID, 'tbodyid')

        # finding elements of product list on the web page
        product_items = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card h-100"]')))
        # creating an empty dict
        products_name_and_price = {}

        # iterating over the list of products and extracting their name and price
        for item in product_items:
            nameElements = item.find_element(By.CLASS_NAME, 'hrefch')
            name = nameElements.text
            priceElement = item.find_element(By.TAG_NAME, "h5")
            price = int(priceElement.text[1:])
            products_name_and_price[name] = price
        print(products_name_and_price)

        # defining a function to get item's price using its name

        def get_price_of_item(item_name):
            return products_name_and_price[item_name]

        # finding the item with the highest price

        max_key = max(products_name_and_price, key=get_price_of_item)
        max_value = products_name_and_price[max_key]
        print(f"The highest price item is {max_key}, it\'s price is ${max_value}")
