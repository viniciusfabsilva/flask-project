import os 
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import current_app as app
from src.ext.auth.models import User
from src.ext.db import db
# CONTROLLER RESOLVE OS PROBLEMS DOS USUARIOS
ALG = "pbkdf2:sha256"


def create_user(email: str, password: str, admin: bool = False) -> User:
    user = User(
      email=email, 
      passwd = generate_password_hash(password, ALG),
      admin=admin,
    )
    db.session.add(user)
    #TODO tratar exception caso o user ja exista
    db.session.commit()
    return user


def save_user_foto(filename, filestorage):
  """
  Saves user foto in
  ./uploads/foo/fsadssd.ext
  """
  filename = os.path.join(
    app.config["UPLOAD_FOLDER"],
    secure_filename(filename)
  )
  #TODO verificar se o diretório existe
  #TODO criar o diretorio
  filestorage.save(filename)