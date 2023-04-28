from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from .models import User, Course
from . import db
from flask_principal import Principal, Permission, RoleNeed, UserNeed, Identity, AnonymousIdentity, identity_changed 
from datetime import datetime

admin_permission = Permission(RoleNeed('admin'))
teacher_permission = Permission(RoleNeed('teacher'))
student_permission = Permission(RoleNeed('student'))

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember = True)
                login_manager.session['firstName'] = user.firstName
                return redirect(url_for('views.profile'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')
            
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully!", category="success")
    return redirect(url_for('views.landing'))


@auth.route('/signup', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        username = request.form.get('username')
        lastName = request.form.get('lastName')
        password = request.form.get('password1')
        passwordConfirm = request.form.get('password2')
        userType = request.form.get('radioUserType')

        userEMail = User.query.filter_by(email = email).first()
        userUsername = User.query.filter_by(username = username).first()

        if userEMail:
            flash('This email already exists, please login instead.', category = 'error')
        elif userUsername:
            flash('This username already exists, please user another username.', category = 'error')
        elif password != passwordConfirm:
            flash('Passwords must match', category='error')
        elif len(password) < 8:
            flash('Passwords must be 8 or more characters', category='error')
        else:
            if userType == "Teacher":
                new_user = User(email = email, username=username, firstName = firstName, lastName = lastName, password = generate_password_hash(password, method = 'pbkdf2:sha256'), roleid = 2)
            else:
                new_user = User(email = email, firstName = firstName, lastName = lastName, password = generate_password_hash(password, method = 'pbkdf2:sha256'), roleid = 1)
            db.session.add(new_user)
            db.session.commit()
            flash('User Created!', category='success')
            return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html')

@auth.route('/createcourse', methods=['GET', 'POST'])
@login_required
def createCourse():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        date_start = request.form.get('date_start')
        date_end = request.form.get('date_end')
        date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
        date_end = datetime.strptime(date_end, '%Y-%m-%d').date()
        course_information = request.form.get('course_information')

        if datetime.now().date() > date_start:
            flash('The starting date has already passed!',category="error")

        elif datetime.now().date() > date_end:
            flash("The end date has already passed!", category="erorr")

        elif date_start > date_end:
            flash("The end date is before the start date!", category="error")

        else:
            new_course = Course(teacherid = current_user.id ,courseName=course_name, dateStart = date_start, dateEnd = date_end, courseInformation = course_information)   
            db.session.add(new_course)
            db.session.commit()
            flash("Course created!", category="success")
        
        return redirect(url_for('auth.createCourse'))
    else:        
        return render_template("auth/createCourse.html")

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == "GET":
        courses_joined = current_user.following()
        return(render_template("profile.html", courses_joined))
    else:
        new_email = request.form.get("new_email")
        new_username = request.form.get("new_username")
        new_firstName = request.form.get("new_firstName")
        new_lastName = request.form.get("new_lastName")
        
        userEmail = User.query.filter_by(email = new_email).first()
        userUsername = User.query.filter_by(username = new_email).first()

        if userEmail:
            flash("Email already exists in the database.", category="error")
        else:
            if new_email != "":
                current_user.email = new_email
        
        if userUsername:
            flash("Username already exists in the database.", category="error")
        else:
            if new_username != "":
                current_user.username = new_username

        if new_firstName != "":
            current_user.firstName = new_firstName
        
        if new_lastName != "":
            current_user.lastName = new_lastName
        
        db.session.commit()

        flash('Your account has been updated!', category="success")
        return redirect(url_for("auth.profile"))
    
@auth.route("/join", methods =["GET","POST"])
@login_required
def join():
    if request.method == "POST":
        course_name = request.form.get('course_name')
        course = Course.query.filter_by(courseName = course_name).first()
        current_user.following.append(course)
        db.session.commit()

        flash("Course joined successfully!", category="success")
        return redirect(url_for("auth.profile"))
    else:
        courses = Course.query.all()
        return render_template("join.html", courses=courses)
