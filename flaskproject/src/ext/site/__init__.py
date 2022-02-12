from .main import bp


# factory
def init_app(app):
    app.register_blueprint(bp)