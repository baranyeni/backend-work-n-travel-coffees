from flask import Flask, render_template
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy

# routes
from app.routes.ShopRouter import ShopRouter

# -- Configuration -- #
app = Flask(__name__,
            static_url_path='/assets',
            static_folder='web/static',
            template_folder='web/templates')

app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'config/locales/translations'
app.register_blueprint(ShopRouter, url_prefix='/shops')
app.config.from_pyfile('config/project.py')
babel = Babel(app, default_locale="en")
db = SQLAlchemy(app)


@babel.localeselector
def get_locale():
    return 'en'


@app.route('/')
def index():
    return render_template("app/index/index.html")


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.debug = True
    app.run()
