from flask import jsonify


class ShopController:
    def __init__(self):
        pass

    def list():
        from app.models.Shop import Shop
        shops = Shop.query.all()

        return jsonify(list(map(lambda shop: build_response(shop), shops)))


def build_response(shop):
    return {
        'id': shop.id,
        'name': f'best_coffee_shop_{shop.id}',
        'rating': shop.id,
        'ratingCount': shop.id * shop.id,
        'city': f'city_name_{shop.id}',
        'address': f'address_text_{shop.id}',
        'imageUrl': shop.imageUrl
    }