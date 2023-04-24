from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

students = db.Table('students',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    creationDate = db.Column(db.DateTime(timezone = True), default = func.now())
    roleid = db.Column(db.Integer)
    following = db.relationship('Course', secondary = students , backref = "followers")
    #Roles: 
    #Student = 1
    #Teacher = 2
    #Admin = 3

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    teacherid = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    dateStart = db.Column(db.Date)
    dateEnd = db.Column(db.Date)
    courseInformation = db.Column(db.String(1000))
    students = db.relationship('User', backref='course', lazy=True) #When adding to class, authenticate, then user.id.course.append(course.id)

