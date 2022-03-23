import os
from project.server import create_app

if __name__ == "__main__":
    app_settings = os.getenv(
        'APP_SETTINGS',
        'project.server.config.DevelopmentConfig'
    )
    app_settings = 'project.server.config.DevelopmentConfig'
    create_app(app_settings)
