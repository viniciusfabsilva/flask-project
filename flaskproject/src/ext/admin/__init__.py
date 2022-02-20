from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.ext.db import db
from src.ext.db.models import Category
admin = Admin()


def init_app(app):
    admin.name = "Comilao Foods"
    admin.template_mode = "bootstrap2"
    admin.init_app(app) 

    admin.add_view(ModelView(Category, db.session))