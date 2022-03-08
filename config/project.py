import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), 'env/.env.development'))

# Secret key
SECRET_KEY = os.urandom(12)

# Babel settings
BABEL_TRANSLATION_DIRECTORIES = 'config/locales/translations'

# Database connection string
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_CONNECTION_STRING")
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
