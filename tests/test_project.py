from app.models import User, Course
from werkzeug.security import generate_password_hash
from app import db
import datetime

def test_landing(client):
    response = client.get("/")
    assert b"<h1><u> Landing Page </u></h1>" in response.data
    assert b"<title> Align </title>" in response.data

def test_login(client):
    response = client.get("/login")
    assert b"<h1><u> Login Page </u></h1>" in response.data
    assert b"Sign Up Here! </a></p>" in response.data

def test_signup_success(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "123456789", "password2": "123456789", "roleid":"1" })
    with app.app_context():
       assert User.query.count() == 1
       assert User.query.first().email == "admin@test.com"
    #Do i need to delete query after?

def test_signup_password_length_fail(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "1", "password2": "1", "roleid":"1" })
    with app.app_context():
        assert User.query.count() == 0
    #Make flash prompt, then how to check for the message?

def test_signup_password_confirm_fail(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "123456789", "password2": "1", "roleid":"1" })
    with app.app_context():
        assert User.query.count() == 0

def test_signup_email_fail(client, app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        db.session.add(new_student)
        db.session.commit()

    response = client.post("/signup", data={"email": 'student@test', "firstName": "student", "lastName": "test", "password1": "123456789", "password2": "123456789", "roleid":"1" })
    with app.app_context():
        assert User.query.count() == 1

def test_course(client, app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add_all([new_student, new_teacher])
        db.session.commit()
        new_course = Course(teacher_id = 1, dateStart = datetime.datetime(2010, 10, 10), dateEnd = datetime.datetime(2010, 11, 10))
        db.session.add(new_course)
        db.session.commit()

        new_student.following.append(new_course)
        db.session.commit()

        assert Course.query.count() == 1
        assert len(new_student.following) == 1
        assert len(new_course.followers) == 1