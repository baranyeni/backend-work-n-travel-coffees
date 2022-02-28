from flask import jsonify
import requests as req
import random


class ShopController:
    def __init__(self):
        pass

    def list():
        return build_shops()


def build_shops():
    response = []
    for i in range(1, 5):
        response.append(build_response(i))

    return jsonify(response)


def build_response(uid):
    rate = random.randint(1, 5)
    user_count = random.randint(0, 10)
    return {
        'id': uid,
        'name': f'best_coffee_shop_{uid}',
        'rating': rate,
        'ratingCount': rate * user_count,
        'city': f'city_name_{uid}',
        'address': f'address_text_{uid}',
        'imageUrl': build_image_url('https://picsum.photos/1800/900')
    }


def build_image_url(url):
    img = req.get(url)
    return img.url
