from app.models import User, Course
from werkzeug.security import generate_password_hash
from app import db
from datetime import datetime, timedelta, date
#make longer test names to ensure the test name is more concise
#inspect DOM to find if div class is there or check for a cookie.
#Look for a header in the response for the flash messages
#Look in test response subclass, in response class in werkzeug

#look into unittest.mock 

def test_should_pass_landing_page_view(client):
    response = client.get("/")
    assert b"<h1><u> Landing Page </u></h1>" in response.data
    assert b"<title> Align </title>" in response.data
    assert response.status_code == 200

def test_should_pass_login_page(client):
    response = client.get("/login")
    assert b"<h1><u> Login Page </u></h1>" in response.data
    assert b"Sign Up Here! </a></p>" in response.data
    assert response.status_code == 200

def test_should_pass_login_all_existing_users(client,app):
    with app.app_context():
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add(new_teacher)
        db.session.commit()
    response = client.post("/login", data={"email": 'admin@test.com', "password":"123456789"})

    with app.app_context():
        #Need to check for flash message even when redirected
        assert response.status_code == 200

def test_should_fail_login_email_wrong(client,app):
    with app.app_context():
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add(new_teacher)
        db.session.commit()
    response = client.post("/login", data={"email": 'teacherWrong@test', "password":"123456789"})
    
    with app.app_context():
        #Need to check for flash message even when redirected. assert b"Incorrect password, try again." in response.data
        assert response.status_code == 200 #status code of 200 to show it hasnt redirected user to a different site.
    
def test_should_fail_password_wrong(client,app):
    with app.app_context():
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add(new_teacher)
        db.session.commit()
    response = client.post("/login", data={"email": 'teacher@test', "password":"1234"})
    
    with app.app_context():
        #Need to check for flash message even when redirected. assert b"Incorrect password, try again." in response.data
        assert response.status_code == 200

def test_should_pass_new_user_signup(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "123456789", "password2": "123456789", "roleid":"1" })
    with app.app_context():
       assert User.query.count() == 1
       assert User.query.first().email == "admin@test.com"
       assert response.status_code == 302

def test_should_pass_signup_has_spaces(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin Space", "lastName": "test Space", "password1": "123456789", "password2": "123456789", "roleid":"1" })
    with app.app_context():
       assert User.query.count() == 1
       assert User.query.first().email == "admin@test.com"
       assert response.status_code == 302

def test_should_pass_signup_password_length(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "1", "password2": "1", "roleid":"1" })
    with app.app_context():
        assert User.query.count() == 0
        assert b"Passwords must be 8 or more characters" in response.data
        assert response.status_code == 200
    #Make flash prompt, then how to check for the message?

def test_should_fail_signup_password_confirm_(client, app):
    response = client.post("/signup", data={"email": 'admin@test.com', "firstName": "admin", "lastName": "test", "password1": "123456789", "password2": "1", "roleid":"1" })
    with app.app_context():
        assert User.query.count() == 0
        assert b"Passwords must match" in response.data
        assert response.status_code == 200

def test_should_fail_signup_email_exists_already(client, app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        db.session.add(new_student)
        db.session.commit()

    response = client.post("/signup", data={"email": 'student@test', "firstName": "student", "lastName": "test", "password1": "123456789", "password2": "123456789", "roleid":"1" })
    with app.app_context():
        assert User.query.count() == 1
        assert b"This email already exists, please login instead." in response.data
        assert response.status_code == 200

def test_should_pass_course_student_join_existing_course(client, app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add_all([new_student, new_teacher])
        db.session.commit()
        new_course = Course(teacherid = 1, dateStart = date(2010, 10, 10), dateEnd = date(2010, 11, 10))
        db.session.add(new_course)
        db.session.commit()

        new_student.following.append(new_course)
        db.session.commit()

        assert Course.query.count() == 1
        assert len(new_student.following) == 1
        assert len(new_course.followers) == 1

def test_should_pass_course_creation(client,app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add_all([new_student, new_teacher])
        db.session.commit()
        client.post("/login", data={"email":"teacher@test", "password":"123456789"})
        response = client.post("/createcourse", data={"date_start":"10-10-2030","date_end":"20-10-2030","course_information":"Auto Testing Course Creation"})

    with app.app_context():
        assert Course.query.count() == 1
        assert Course.query.first().courseInformation == "Auto Testing Course Creation"

def test_should_fail_course_creation_date_already_started(client,app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add_all([new_student, new_teacher])
        db.session.commit()
        
        date_now = datetime.now().date()
        date_start = date_now - timedelta(days=10)
        date_end = date_now + timedelta(days=20)

        date_start= datetime.strftime(date_start, "%d/%m/%Y")
        date_end = datetime.strftime(date_end, "%d/%m/%Y")

        client.post("/login", data={"email":"teacher@test", "password":"123456789"})
        response = client.post("/createcourse", data={"date_start":date_start,"date_end":date_end ,"course_information":"Auto Testing Course Creation"})

    with app.app_context():
        assert Course.query.count() == 0

def test_should_fail_course_creation_date_already_ended(client,app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add_all([new_student, new_teacher])
        db.session.commit()
        
        date_now = datetime.now().date()
        date_start = date_now + timedelta(days=10)
        date_end = date_now - timedelta(days=10)

        date_start= datetime.strftime(date_start, "%d/%m/%Y")
        date_end = datetime.strftime(date_end, "%d/%m/%Y")

        client.post("/login", data={"email":"teacher@test", "password":"123456789"})
        response = client.post("/createcourse", data={"date_start":date_start,"date_end":date_end ,"course_information":"Auto Testing Course Creation"})

    with app.app_context():
        assert Course.query.count() == 0

def test_should_fail_course_creation_end_date_before_start_date(client,app):
    with app.app_context():
        new_student = User(email = "student@test", firstName = "student", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 1)
        new_teacher = User(email = "teacher@test", firstName = "teacher", lastName = "test", password = generate_password_hash("123456789", method = 'pbkdf2:sha256'), roleid = 2)
        db.session.add_all([new_student, new_teacher])
        db.session.commit()
        
        date_now = datetime.now().date()
        date_start = date_now + timedelta(days=20)
        date_end = date_now + timedelta(days=10)

        date_start= datetime.strftime(date_start, "%d/%m/%Y")
        date_end = datetime.strftime(date_end, "%d/%m/%Y")

        client.post("/login", data={"email":"teacher@test", "password":"123456789"})
        response = client.post("/createcourse", data={"date_start":date_start,"date_end":date_end ,"course_information":"Auto Testing Course Creation"})

    with app.app_context():
        assert Course.query.count() == 0