from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template('landing.html')

@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/user/<firstName>')
@login_required
def user(firstName):
    user = User.query.filter_by(firstName = firstName).first_or_404()
    courses = user.following
    return render_template('user.html', user=user, courses=courses)
    