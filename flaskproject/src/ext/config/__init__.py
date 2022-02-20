def init_app(app):
  app.config["SECRET_KEY"] = "1231241241223123123"
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comilao.db"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

  if app.debug:
    app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
    app.config['DEBUG_TB_PROFILER_ENABLED'] = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
