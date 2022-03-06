from flask import Flask, render_template
from flask_babel import Babel, gettext, _

from app.routes.ShopRouter import ShopRouter

app = Flask(__name__,
            static_url_path='/assets',
            static_folder='web/static',
            template_folder='web/templates')

app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'config/locales/translations'

babel = Babel(app, default_locale="en")


@babel.localeselector
def get_locale():
    return 'en'


# TODO: Create view and render rich content
@app.route('/')
def index():
    print(gettext('File.Not.Found'))
    print(_('File.Not.Found'))
    return render_template("app/index/index.html")


# -- Configuration -- #


app.register_blueprint(ShopRouter, url_prefix='/shops')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.debug = True
    app.run()
