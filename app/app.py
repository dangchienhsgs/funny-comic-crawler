from flask import Flask

from .main_content import views


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprint(app)

    return app


def register_blueprint(app):
    app.register_blueprint(views.blueprint)


