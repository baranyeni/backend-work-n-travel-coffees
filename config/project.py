import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), 'env/.env.development'))

# Application config
ENV = os.environ.get("ENV")
TESTING = os.environ.get("TESTING")
DEBUG = os.environ.get("DEBUG")

# Secret key
SECRET_KEY = os.urandom(12)

# Babel settings
BABEL_TRANSLATION_DIRECTORIES = 'config/locales/translations'

# Database connection string
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_CONNECTION_STRING")
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

# Flask Admin theme
FLASK_ADMIN_SWATCH = 'cerulean'
