from flask import Blueprint
from app.controllers.UserController import UserController

UserRouter = Blueprint('UserController', __name__)
UserRouter.route('/authorize_check/', methods=['POST'])(UserController.authorize_check)
UserRouter.route('/log_out/', methods=['POST'])(UserController.logout)
