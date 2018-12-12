#coding: UTF-8
import selenium
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
    omulette_list = []
    bs = BeautifulSoup(page_source, "html.parser")
    div_item_list = bs.select("ul.js-rstlist-info")
    for item_list in div_item_list[0].select("div.list-rst__wrap"):
        img_tags = item_list.select("img.js-cassette-img")

        img = img_tags[0].get("data-original")

        item_name_tags = item_list.select("a.list-rst__rst-name-target")
        url = item_name_tags[0].get("href")

        name = item_list.find('a').text

        omulette = {"name": name, "img": img, "restaurant": url}
        omulette_list.append(omulette)
    return omulette_list
