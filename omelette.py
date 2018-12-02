from flask import Flask, render_template, request, redirect
import Scraping
import time
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def send_text():
    return render_template('index.html')


@app.route("/display", methods=['POST', 'GET'])
def index():
    s = "レストラン"
    location = request.form['location']
    Scraping.extraction(Scraping.search(location))

    dic = dict(zip(Scraping.omulette_restaurant,
                   Scraping.omulette_img, Scraping.omulette_name))
    restaurants = dic.items()

    return render_template('index.html', s=s, restaurants=restaurants)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


'''
    f = open('main.json', 'w')

    json.dump(dic, f)
    f.close()

    f = open('main.json', 'r')

    jsonData = json.load(f)

    restaurants = jsonData.keys()
    images = jsonData.values()
    f.close()
    print(jsonData)
'''
