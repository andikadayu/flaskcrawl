import json
from flask import Flask, request, jsonify
from models.shopeeCrawl import shopeeCrawl

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return f'Hello, World!'


@app.route('/api/shopee/get/<url>', methods=['GET'])
def get_shopee(url):
    shopee = shopeeCrawl(url)
    return jsonify(shopee.get_shopee())
