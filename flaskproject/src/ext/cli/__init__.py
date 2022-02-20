import click
from src.ext.db import db
from src.ext.db import models  # noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("Lista de pedidos")


