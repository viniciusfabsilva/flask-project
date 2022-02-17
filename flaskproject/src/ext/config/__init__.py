def init_app(app):
  app.config["SECRET_KEY"] = "july"
  app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comilao.db'

  if app.debug:
    app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
    app.config['DEBUG_TB_PROFILER_ENABLED'] = True