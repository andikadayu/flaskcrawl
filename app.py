import json
from flask import Flask, request, jsonify
from models.shopeeCrawl import shopeeCrawl

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return f'Hello, World!'


@app.route('/api/shopee/get', methods=['GET'])
def get_shopee():
    # urls = request.args.get('url')
    urls = "https://shopee.co.id/(BISA-COD)-Rubik-3x3-MoYu-Meilong-Magic-Cube-3x3x3-Speed-Cube-i.151487611.11975266198?sp_atk=e54b0222-90c3-4461-a9d6-4d115a59c0a9&xptdk=e54b0222-90c3-4461-a9d6-4d115a59c0a9"
    shopee = shopeeCrawl(urls)
    return jsonify(shopee.get_shopee())
