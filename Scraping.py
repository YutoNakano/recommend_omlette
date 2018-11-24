from selenium import webdriver
from bs4 import BeautifulSoup


def search(place_name):

    driver = webdriver.Chrome()
    driver.get("https://tabelog.com/")
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
        item_name_tags = item_list.select("a.list-rst__rst-name-target")
        i = item_name_tags[0].get("href")
        omulette_restaurant.append(i)

    return omulette_restaurant, omulette_img


omulette_restaurant = []
omulette_img = []

location = input()
