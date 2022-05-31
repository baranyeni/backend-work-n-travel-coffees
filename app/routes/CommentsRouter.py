from flask import Blueprint
from app.controllers.CommentsController import CommentsController

CommentsRouter = Blueprint('CommentsController', __name__)
CommentsRouter.route('/list/', methods=['GET'])(CommentsController.list)
CommentsRouter.route('/create/', methods=['POST'])(CommentsController.create)
