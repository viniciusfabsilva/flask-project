from tkinter import Button
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from src.ext.auth.models import User
from src.ext.db import db
from flask import flash, Markup


def format_user(self, request, user, *args):
    return user.email.split("@")[0]


class UserAdmin(ModelView):
    """Interface admin de user"""
    column_formatters = {
        "email": format_user
    }

    column_list = ["email", "admin", "nome"]

    column_searchable_list = ["email"]
    column_filters = [
      "email", 
      "admin",
      filters.FilterLike(
        User.email,
        "dominio",
        options=(("gmail", "Gmail"), ("uol", "Uol"))
      )
      ]

    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toogle_admin',
        'Toggle admin status',
        'Are you sure?'
    )
    def toogle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} Usuários alterados com sucesso!", "Success")

    @action(
        'send_email',
        'send email to all users',
        'Are you sure?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # redirect para um form para escrever a mensagem do email
        # enviar o email
        flash(f"{len(users)} emails enviados.!", "Success")
