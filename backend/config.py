from os import environ, path
from dotenv import load_dotenv

# Application's main directory
basedir = path.abspath(path.dirname(__file__))
# Specificy a `.env` file containing key/value config values
load_dotenv(path.join(basedir, '.env'))

class Config:
    ENVIRONMENT = environ.get("ENVIRONMENT")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") or \
        "postgresql://user:password@localhost/lastpuff"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY") or "dev_key"