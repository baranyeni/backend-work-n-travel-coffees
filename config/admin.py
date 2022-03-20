import flask_login

from app import db
from app.models.Shop import Shop
from app.models.User import User
from flask_login import current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    admin = Admin(app, name=app.name, template_mode='bootstrap3')

    admin.add_view(SecureModelView(Shop, db.session))
    admin.add_view(SecureModelView(User, db.session))


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()
