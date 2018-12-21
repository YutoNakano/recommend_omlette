#coding: UTF-8
from jinja2 import Template, Environment, FileSystemLoader
from jsonData import writeData
from Scraping import search, extraction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import Scraping
from flask import Flask, render_template, request
from Twitter import tweet_search

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def send_text():
    return render_template('index.html')


@app.route("/display", methods=['POST', 'GET'])
def index():
    s = "レストラン"
    location = request.form['location']
    dic_result = writeData(Scraping.extraction(search(location)))
    print(dic_result)
    restaurant_name = dic_result[0]["name"]
    tweet = tweet_search(location, restaurant_name)
    print(location)
    print(restaurant_name)
    return render_template('index.html', restaurants=dic_result, tweet_contents=tweet)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
