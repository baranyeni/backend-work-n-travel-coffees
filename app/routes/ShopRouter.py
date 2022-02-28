from flask import Blueprint

from app.controllers.ShopController import ShopController

ShopRouter = Blueprint('ShopController', __name__)
ShopRouter.route('/list/', methods=['GET'])(ShopController.list)
