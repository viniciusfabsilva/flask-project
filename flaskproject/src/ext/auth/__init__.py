from src.ext.auth import models
from src.ext.auth.commands import list_users, add_user  # noqa

from src.ext.db import db
from src.ext.auth.admin import UserAdmin
from src.ext.admin import admin
from src.ext.auth.models import User


def init_app(app):
    """TODO: inicializar flask simple login"""
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))
