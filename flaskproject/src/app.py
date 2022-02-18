from flask import Flask
from src.ext import site
from src.ext import config
from src.ext import toolbar
from src.ext import db
from src.ext import migrate
from src.ext import cli

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app