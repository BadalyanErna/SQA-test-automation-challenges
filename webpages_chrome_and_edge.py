import time
from selenium import webdriver


def open_website_on_chrome():
    chromedriver = webdriver.Chrome()
    chromedriver.get("https://www.demoblaze.com/")
    time.sleep(3)


def open_website_on_edge():
    edgedriver = webdriver.Edge()
    edgedriver.get("https://www.demoblaze.com/")
    time.sleep(3)


open_website_on_chrome()
open_website_on_edge()
