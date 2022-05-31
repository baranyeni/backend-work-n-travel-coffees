from flask import jsonify, request
from flask_login import login_required
from app.models.Shop import Shop
from flasgger import swag_from
from app.models import db
from sqlalchemy.exc import IntegrityError


class ShopController:
    def __init__(self):
        pass

    # @login_required
    @swag_from('../../config/docs/shops/list.yml')
    def list():
        from app.models.Shop import Shop
        shops = Shop.query.all()
        return jsonify(list(map(lambda shop: build_response_list(shop), shops)))

    @login_required
    # @swag_from('../../config/docs/shops/create.yml')
    def create():
        try:
            name = request.form.get('name')
            rating = request.form.get('rating')
            ratingCount = request.form.get('ratingCount')
            address = request.form.get('address')
            imageUrl = request.form.get('imageUrl')

            item = Shop(name=name, rating=rating, ratingCount=ratingCount, address=address, imageUrl=imageUrl)
            db.session.add(item)
            db.session.commit()
            return {"status": 200}
        except IntegrityError as err:
            db.session.rollback()
            return str(err)
        except:
            db.session.rollback()
            return {"status": 404}
        finally:
            db.session.close()


def build_response_list(shop):
    return {
        'id': shop.id,
        'name': shop.name,
        'rating': shop.rating,
        'ratingCount': shop.ratingCount,
        'city': f'city_name_{shop.id}',
        'address': shop.address,
        'imageUrl': shop.imageUrl,
        "comments": build_comment_object(shop.comments)
    }


def build_comment_object(comments):
    comments_json = []
    for comment in comments:
        comments_json.append({
            'id': comment.id,
            'user_id': comment.user_id,
            'shop_id': comment.shop_id,
            'text': comment.text
        })
    return comments_json