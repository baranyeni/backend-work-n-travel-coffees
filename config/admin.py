from app import db
from app.models.Shop import Shop
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    admin = Admin(app, name=app.name, template_mode='bootstrap3')

    admin.add_view(SecureModelView(Shop, db.session))


class SecureModelView(ModelView):
    def is_accessible(self):
        return True  # TODO: Change this into session check
