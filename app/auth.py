from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, login_manager

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<h1> Login Page <h1>'

@auth.route('/signup')
def signup():
    return '<h1> Signup Page <h1>'