from flask_login import LoginManager, login_manager
from src.ext.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return True


def init_app(app):
    lm = LoginManager()
    lm.login_view = 'auth.login'
    lm.init_app(app)
