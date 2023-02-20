import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# navigating to the main page
driver.get("https://www.demoblaze.com/")

# opening the phones section
driver.find_element(By.XPATH, '//a[@onclick="byCat(\'phone\')"]').click()
time.sleep(5)
# finding elements of phones list on the web page
phones = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
# creating an empty dict
phones_name_and_price = {}

# iterating over the list of phones and extracting their name and price
for phone in phones:
    nameElements = phone.find_element(By.CLASS_NAME, 'hrefch')
    name = nameElements.text
    priceElement = phone.find_element(By.TAG_NAME, "h5")
    price = int(priceElement.text[1:])
    phones_name_and_price[name] = price
print(phones_name_and_price)


# defining a function to get it's price using it's name
def get_price_of_phone(phone_name):
    return phones_name_and_price[phone_name]


# finding the phone with the highest price
max_key = max(phones_name_and_price, key=get_price_of_phone)
max_value = phones_name_and_price[max_key]
print(f"The highest phone is {max_key} and the price is ${max_value}")

driver.quit()
