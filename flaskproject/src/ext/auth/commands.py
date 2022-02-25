import click
from src.ext.auth.models import User
from src.ext.auth.controller import create_user

#TODO mover para controllers
def list_users():
    users = User.query.all()
    click.echo(f"Lista de usuarios: \n {users} \n")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    #TODO Tratar user exists exception
    create_user(
        email=email,
        password=passwd,
        admin=admin
    )

    click.echo(f"Usuário {email} criado com sucesso!")
