import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), 'env/.env.development'))

# Application config
ENV = os.environ.get("ENV")
TESTING = os.environ.get("TESTING")
DEBUG = os.environ.get("DEBUG")

# Secret key
SECRET_KEY = f'{os.environ.get("SECRET_KEY")}_SECRET_KEY'

# Babel settings
BABEL_TRANSLATION_DIRECTORIES = '../config/locales/translations'

# SQLAlchemy configurations
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_CONNECTION_STRING")
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
SQLALCHEMY_RECORD_QUERIES = os.environ.get("SQLALCHEMY_RECORD_QUERIES")
SQLALCHEMY_POOL_SIZE = int(os.environ.get("SQLALCHEMY_POOL_SIZE"))
SQLALCHEMY_POOL_TIMEOUT = int(os.environ.get("SQLALCHEMY_POOL_TIMEOUT"))
SQLALCHEMY_POOL_RECYCLE = int(os.environ.get("SQLALCHEMY_POOL_RECYCLE"))
SQLALCHEMY_MAX_OVERFLOW = int(os.environ.get("SQLALCHEMY_MAX_OVERFLOW"))

# Flask Admin theme
FLASK_ADMIN_SWATCH = 'cerulean'
