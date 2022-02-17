import click
from src.ext.db import db
from src.ext.site import models 


def init_app(app):
  
  @app.cli.command()
  def create_db():
      """Este comando inicializa o db"""
      db.create_all()
  

  @app.cli.command()
  @click.option("--email", "-e")
  @click.option("--paswd", "-p")
  @click.option("--admin", "-a", is_flag=True, default=False)
  def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    user = models.User(
      email=email,
      passwd=passwd,
      admin=admin
    )
    db.session.add(user)
    db.session.commit()

  @app.cli.command()
  def listar_pedidos():
    # TODO: usar tabulate
    click.echo("Lista de pedidos")

  @app.cli.command()
  def listar_usuarios():
    click.echo("Lista de usuarios")
