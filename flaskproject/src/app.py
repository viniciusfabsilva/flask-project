from flask import Flask
from src.ext import site
from src.ext import config
from src.ext import toolbar

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app