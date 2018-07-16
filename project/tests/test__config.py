# project/server/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        
        self.assertFalse(app.config['SECRET_KEY'] is  b'\xee\xf3\xd1a\x97bf\x80\x1b~\xc8]9\xa6^$\xe8\x9d\x88e\xea\x12\\.')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///test.db'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        
        self.assertFalse(app.config['SECRET_KEY'] is  b'\xee\xf3\xd1a\x97bf\x80\x1b~\xc8]9\xa6^$\xe8\x9d\x88e\xea\x12\\.')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///test.db'
        )

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
