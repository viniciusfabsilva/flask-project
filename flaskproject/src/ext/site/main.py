import re
from flask import flash, render_template
from flask import Blueprint
from flask import current_app as app
from flask import request
from flask import redirect, url_for
from flask_login import login_user, logout_user
from src.ext.auth.form import UserForm
from src.ext.auth.form import LoginForm
from src.ext.site.controllers import get_items
from src.ext.auth.models import User
from src.ext.auth.controller import create_user, save_user_foto

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    # current_app.logger.debug("entrei na função main") << ferramenta de debug para o toolbar
    return render_template("index.html", get_item = get_items())


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            password=form.password.data
        )
        foto = request.files.get('foto')
        if foto:
            save_user_foto(
                foto.filename,
                foto
            )

        # TODO forçar login
        return redirect("/")

    return render_template("userform.html", form=form)


@bp.route("/restaurantes")
def restaurants():
    get_item = get_items()
    return render_template("restaurants.html", get_item = get_item)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        if user and user.passwd == form.password.data:
            flash('Logged in.')
            return redirect("/")
        else:
            flash('Invalid Login.')
    else:
        print(form.errors)

    return render_template("loginform.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
