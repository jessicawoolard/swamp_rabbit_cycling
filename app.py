from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get('https://api.etsy.com/v2/listings/active?api_key=cdwxq4soa7q4zuavbtynj8wx&keywords=bicycle&includes=Images,Shop&sort_on=score')

    data = response.json()
    print(data)

    etsy_listings = data['results']

    photos = []

    for etsy_listing in etsy_listings:
        # photos.append(

        print(etsy_listing['Images'])

    # planet_html = ''.join(planet_html)

    # Get html and render to screen
    index_file = open('index.html', 'r')
    index_html = index_file.read()
    # index_html = index_html.replace('{{planet_list}}', planet_html)
    index_file.close()

    return index_html
