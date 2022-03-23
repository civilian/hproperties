# project/server/__init__.py
import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app_settings = os.getenv(
        'APP_SETTINGS',
        'project.server.config.DevelopmentConfig'
    )
    app.config.from_object(app_settings)

    from .orm import BaseManager
    BaseManager.set_connection(database_settings=app.config['DB_SETTINGS'])

    from project.server.property.views import property_blueprint
    app.register_blueprint(property_blueprint)

    return app
