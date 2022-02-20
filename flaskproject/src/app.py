from flask import Flask
from src.ext import site
from src.ext import config
from src.ext import toolbar
from src.ext import db
from src.ext import migrate
from src.ext import cli
from src.ext import auth
from src.ext import hooks
from src.ext import admin


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)
    return app
