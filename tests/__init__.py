import unittest
from app import app, db
from config import TestConfig
from modelos.persona import Persona
from modelos.red_social import RedSocial
from modelos.asignacion import Asignacion


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.from_object(TestConfig)
        cls.app = app
        cls.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()


    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            #db.drop_all()
            db.session.remove()

