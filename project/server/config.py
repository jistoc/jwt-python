# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_local_base = 'sqlite:///test.db'
database_name = 'something'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = b'\xee\xf3\xd1a\x97bf\x80\x1b~\xc8]9\xa6^$\xe8\x9d\x88e\xea\x12\\.'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_local_base


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sqlite_local_base
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = b'\xee\xf3\xd1a\x97bf\x80\x1b~\xc8]9\xa6^$\xe8\x9d\x88e\xea\x12\\.'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = sqlite_local_base
