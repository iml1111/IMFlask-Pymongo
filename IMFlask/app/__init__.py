"""
Application Factory Module
"""
from flask import Flask
from config import config
from app import api

from app.api.template import template as template_bp
from app.api.error_handler import error_handler as error_bp

def create_app(config_name):
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
        static_url_path='/',
        static_folder='asset/',
        template_folder='asset/'
    )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    api.init_app(app)

    app.register_blueprint(error_bp)
    app.register_blueprint(template_bp)

    return app