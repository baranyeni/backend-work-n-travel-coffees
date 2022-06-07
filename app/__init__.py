from flask import Flask, render_template, session
from flask_babel import Babel
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS

from app.models import db
from config.admin import setup_admin
from config.login import setup_login_manager

# routes
from app.routes.ShopRouter import ShopRouter
from app.routes.CommentsRouter import CommentsRouter
from app.routes.LoginRouter import LoginRouter
from app.routes.UserRouter import UserRouter


# -- Configuration -- #
app = Flask(__name__,
            static_url_path='/assets',
            static_folder='../web/static',
            template_folder='../web/templates')

app.config.from_pyfile('../config/project.py')
app.register_blueprint(ShopRouter, url_prefix='/shops')
app.register_blueprint(CommentsRouter, url_prefix='/comments')
app.register_blueprint(UserRouter, url_prefix='/users')
app.register_blueprint(LoginRouter)

# create db
db.init_app(app)

# create migrate for migration
migrate = Migrate(app, db)

# create babel for localisation
babel = Babel(app, default_locale="en")

# setup the flask-admin panel
setup_admin(app)

# setup the flask-login
setup_login_manager(app)

# setup Swagger docs
swagger = Swagger(app)

# Allow CORS to not to have problem
CORS(app)


@babel.localeselector
def get_locale():
    return 'en'


@app.before_request
def make_session_permanent():
    session.modified = True
    session.permanent = True


@app.after_request
def creds(response):
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


@app.route('/')
def index():
    return render_template("app/index/index.html")
