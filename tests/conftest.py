import pytest
from flask_sqlalchemy import SQLAlchemy
from app import create_app, db

config = "config.TestingConfig"

@pytest.fixture()
def app():
    app = create_app(config)

    print("CREATING DATABASE")
    with app.app_context():
        db.create_all()
    
    yield app

@pytest.fixture()
def client(app):
    yield app.test_client()