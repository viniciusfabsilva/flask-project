from flask import render_template
from flask import Blueprint
from flask import current_app
from flask import request
from flask import redirect
from src.ext.auth.form import UserForm
from src.ext.auth.models import User
from src.ext.auth.controller import create_user, save_user_foto

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    # current_app.logger.debug("entrei na função main") << ferramenta de debug para o toolbar
    return render_template("index.html")


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
    return render_template("restaurants.html")
