from flask import Flask
from flask_babelex import Babel
from flask_migrate import Migrate

from app.models import db
from config.admin import setup_admin
from config.login import setup_login_manager

# routes
from app.routes.ShopRouter import ShopRouter


# -- Configuration -- #
app = Flask(__name__,
            static_url_path='/assets',
            static_folder='../web/static',
            template_folder='../web/templates')

app.config.from_pyfile('../config/project.py')
app.register_blueprint(ShopRouter, url_prefix='/shops')

# create db
db.init_app(app)

# create babel for localisation
babel = Babel(app, default_locale="en")

# create migrate for migration
migrate = Migrate(app, db)

# setup the flask-admin panel
setup_admin(app)

# setup the flask-login
setup_login_manager(app)

@babel.localeselector
def get_locale():
    return 'en'
