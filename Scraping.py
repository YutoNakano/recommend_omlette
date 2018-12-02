from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
import json


def search(place_name):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get("https://tabelog.com/")
    WebDriverWait(driver, 10).until(
        EC.title_contains("食べログ")
    )

    input_elem = driver.find_element_by_name("sa")
    input_elem.send_keys(place_name)

    input_elem.click()

    elem_search_word = driver.find_element_by_name("sk")

    elem_search_word.send_keys("オムライス")

    elem_search_btn = driver.find_element_by_id("js-global-search-btn")

    elem_search_btn.click()
    page_source = driver.page_source

    return page_source


def extraction(page_source):
    bs = BeautifulSoup(page_source, "html.parser")

    div_item_list = bs.select("ul.js-rstlist-info")

    for item_list in div_item_list[0].select("div.list-rst__wrap"):
        img_tags = item_list.select("img.js-cassette-img")

        img = img_tags[0].get("data-original")
        omulette_img.append(img)
        item_restaurant_tags = item_list.select("a.list-rst__rst-name-target")
        i = item_restaurant_tags[0].get("href")
        omulette_restaurant.append(i)

        name = img_tags[0].find_all('a')

        restaurant_name = name.text

        omulette_name.append(restaurant_name)

    return omulette_restaurant, omulette_img, omulette_name


omulette_restaurant = []
omulette_name = []
omulette_img = []
