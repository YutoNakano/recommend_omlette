import Scraping
from flask import Flask, render_template, request

app = Flask(__name__)
Scraping.extraction(Scraping.search(Scraping.location))


restaurants = Scraping.omulette_restaurant
images = Scraping.omulette_img


@app.route("/sendtext", methods=['POST'])
def sendtext():
    return render_template('index.html', title=request.form['message'])


@app.route("/")
def index():
    s = "レストラン"

    return render_template('index.html', s=s, restaurants=restaurants, images=images)


app.run()
