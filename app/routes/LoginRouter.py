from flask import Blueprint
from app.controllers.LoginController import LoginController

LoginRouter = Blueprint('LoginController', __name__)
LoginRouter.route('/signup/', methods=['GET', 'POST'])(LoginController.signup)
LoginRouter.route('/login/', methods=['GET', 'POST'])(LoginController.login)
LoginRouter.route('/logout/', methods=['GET', 'POST'])(LoginController.logout)
