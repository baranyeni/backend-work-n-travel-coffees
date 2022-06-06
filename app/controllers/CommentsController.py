from unicodedata import name
from flask import jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from app.models.Comment import Comment
from flasgger import swag_from
from app.models import db
from sqlalchemy.exc import IntegrityError


class CommentsController:
    def __init__(self):
        pass

    @token_required
    @swag_from('../../config/docs/comments/list.yml')
    def list():
        from app.models.Comment import Comment
        comments = Comment.query.all()
        return jsonify(list(map(lambda comment: build_response_list(comment), comments)))
        
    @token_required
    # @swag_from('../../config/docs/comments/create.yml')
    def create():
        try:
            user_id = request.form.get('user_id')
            shop_id = request.form.get('shop_id')
            text = request.form.get('text')
 
            item = Comment( user_id=user_id,shop_id=shop_id, text = text)
            db.session.add(item)
            db.session.commit()
            return { "status": 200 }
        except IntegrityError as err:
            db.session.rollback()
            return str(err)
        except:  
            db.session.rollback()
            return { "status": 404 }
        finally:
            db.session.close()



def build_response_list(comment):
    return {
        'id': comment.id,
        'user_id': comment.user_id,
        'shop_id': comment.shop_id,
        'text': comment.text,
    }

