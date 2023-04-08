from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from .models import User
from . import db

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


@auth.route('/signup', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password1')
        passwordConfirm = request.form.get('password2')
        userType = request.form.get('radioUserType')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('This email already exists, please login instead.', category = 'error')
        elif password != passwordConfirm:
            flash('Passwords must match', category='error')
        elif len(password) < 8:
            flash('Passwords must be 8 or more characters', category='error')
        else:
            if userType == "Teacher":
                new_user = User(email = email, firstName = firstName, lastName = lastName, password = generate_password_hash(password, method = 'pbkdf2:sha256'), roles = 2)
            else:
                new_user = User(email = email, firstName = firstName, lastName = lastName, password = generate_password_hash(password, method = 'pbkdf2:sha256'), roles = 1)
            db.session.add(new_user)
            db.session.commit()
            flash('User Created!', category='success')
            return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html')