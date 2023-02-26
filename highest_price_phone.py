from selenium import webdriver
from selenium.webdriver.common.by import By
from waits import Wait

driver = webdriver.Chrome()
get_wait = Wait(driver)

# navigating to the main page
driver.get("https://www.demoblaze.com/")

# locating the products elements from the first page
products = get_wait.wait_for_element(By.ID, 'tbodyid')

# finding elements of product list on the web page
product_items = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
# creating an empty dict
products_name_and_price = {}

# iterating over the list of phones and extracting their name and price
for item in product_items:
    nameElements = item.find_element(By.CLASS_NAME, 'hrefch')
    name = nameElements.text
    priceElement = item.find_element(By.XPATH, "//*[@id='tbodyid']/div[4]/div/div/h5")
    price = int(priceElement.text[1:])
    products_name_and_price[name] = price
print(products_name_and_price)


# defining a function to get it's price using it's name
def get_price_of_item(item_name):
    return products_name_and_price[item_name]

    # finding the phone with the highest price


max_key = max(products_name_and_price, key=get_price_of_item)
max_value = products_name_and_price[max_key]
print(f"The highest price item is {max_key}, it\'s price is ${max_value}")

driver.quit()
