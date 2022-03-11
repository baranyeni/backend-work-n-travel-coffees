from app.models import db
from app.models.Shop import Shop
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    admin = Admin(app, name=app.name, template_mode='bootstrap3')

    admin.add_view(ModelView(Shop, db.session))
