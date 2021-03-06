from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.ext.db import db
from src.ext.db.models import Category
from src.ext.db.models import Items
from src.ext.db.models import Store
admin = Admin()


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Comilão Foods")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app) 

    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Items, db.session))
    admin.add_view(ModelView(Store, db.session))