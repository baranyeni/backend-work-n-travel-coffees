from flask import jsonify
from flask_login import login_required


class ShopController:
    def __init__(self):
        pass

    @login_required
    def list():
        from app.models.Shop import Shop
        shops = Shop.query.all()

        return jsonify(list(map(lambda shop: build_response(shop), shops)))


def build_response(shop):
    return {
        'id': shop.id,
        'name': shop.name,
        'rating': shop.rating,
        'ratingCount': shop.ratingCount,
        'city': f'city_name_{shop.id}',
        'address': shop.address,
        'imageUrl': shop.imageUrl
    }
