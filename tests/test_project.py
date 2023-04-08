from app.models import User
from werkzeug.security import generate_password_hash
from app import db

def test_landing(client):
    response = client.get("/")
    assert b"<h1><u> Landing Page </u></h1>" in response.data
    assert b"<title> Align </title>" in response.data

def test_login(client):
    response = client.get("/login")
    assert b"<h1><u> Login Page </u></h1>" in response.data
    assert b"Sign Up Here! </a></p>" in response.data

def test_signup_success(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "123456789", "password2": "123456789", "roles":"1" })
    with app.app_context():
       assert User.query.count() == 1
       assert User.query.first().email == "admin@test.com"
    #Do i need to delete query after?

def test_signup_password_fail(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "1", "password2": "1", "roles":"1" })
    with app.app_context():
        assert User.query.count() == 0
    #Make flash prompt, then how to check for the message?

def test_signup_email_fail(client, app):
    with app.app_context():
        new_user = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roles = 1)
        db.session.add(new_user)
        db.session.commit()

    response = client.post("/signup", data={"email": 'student@test', "firstName": "student", "lastName": "test", "password1": "123456789", "password2": "123456789", "roles":"1" })
    with app.app_context():
        assert User.query.count() == 1


