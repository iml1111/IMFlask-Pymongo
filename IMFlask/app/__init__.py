"""
Application Factory Module
"""
from flask import Flask
from app import api

# Routes
from app.api.template import template as template_bp
from app.api.error_handler import error_handler as error_bp
from app.api.sample_api import sample_api as sample_api_bp


def create_app(config):
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
        static_url_path='/',
        static_folder='asset/',
        template_folder='asset/'
    )
    app.config.from_object(config)
    config.init_app(app)
    api.init_app(app)

    app.register_blueprint(error_bp)
    app.register_blueprint(template_bp)
    app.register_blueprint(sample_api_bp, url_prefix='/sample/')

    return app