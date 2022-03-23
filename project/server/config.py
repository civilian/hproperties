import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    DB_SETTINGS = {
        'host': os.getenv('MYSQL_HOST', 'localhost'),
        'port': os.getenv('MYSQL_PORT', '3306'),
        'database': os.getenv('MYSQL_DB', 'db'),
        'user': os.getenv('MYSQL_USER', 'root'),
        'password': os.getenv('PASSWORD', 'my_precious'),
    }


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    # BaseConfig.DB_SETTINGS.update(
    #     {'database': BaseConfig.DB_SETTINGS['database']+'test'}
    # )


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
