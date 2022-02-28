from flask import Flask, jsonify
import requests as req
import random

app = Flask(__name__)

# TODO: Create view and render rich content
@app.route('/')
def index():
    return "Only to make sure that server is up n running"

@app.route('/shops/')
def shops():
    return build_shops()

def build_shops():
    response = []
    for i in range(1, 5):
        response.append(build_response(i))

    return jsonify(response)

def build_response(id):
    rate      = random.randint(1, 5)
    userCount = random.randint(0, 10)
    return {
        'id': id,
        'name': f'best_coffee_shop_{id}',
        'rating': rate,
        'ratingCount': rate*userCount,
        'city': f'city_name_{id}',
        'address': f'address_text_{id}',
        'imageUrl': build_image_url('https://picsum.photos/1800/900')
        }

def build_image_url(url):
    img = req.get(url)
    return img.url