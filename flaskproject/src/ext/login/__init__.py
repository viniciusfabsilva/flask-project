from flask_login import LoginManager
from src.ext.auth.models import User

login_manager = LoginManager()

def init_app(app):
    login_manager.init_app(app)
    login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()