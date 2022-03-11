from flask import Flask, render_template
from flask_babelex import Babel
from app.models import db
from config.admin import setup_admin

# routes
from app.routes.ShopRouter import ShopRouter

# -- Configuration -- #
app = Flask(__name__,
            static_url_path='/assets',
            static_folder='web/static',
            template_folder='web/templates')

app.config.from_pyfile('config/project.py')
app.register_blueprint(ShopRouter, url_prefix='/shops')


# create babel for localisation
babel = Babel(app, default_locale="en")

# Setup the flask-admin panel
setup_admin(app)


@babel.localeselector
def get_locale():
    return 'en'


@app.route('/')
def index():
    return render_template("app/index/index.html")


if __name__ == '__main__':
    app.debug = True
    db.init_app(app)
    app.run()
