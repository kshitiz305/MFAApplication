"""
auth.py
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """Render login page"""
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    """User login"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # Reload page if user not exist or wrong password
    # check if user has admin role
    if not user.role == 'Admin':
        flash('Access denied You are not authorized to access this page.')
        return redirect(url_for('auth.login'))  # Reload page if user is not admin

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('main.profile'))


@auth.route('/create')
def create():
    """Render create page"""
    return render_template('create.html')


@auth.route('/create', methods=['POST'])
def create_post():
    """Create User"""
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to create page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.create'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'), role=role)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    flash('User Created')
    return redirect(url_for('auth.create'))

@auth.route('/update')
def update():
    """Render update page"""
    return render_template('update.html')

@auth.route('/update', methods=['POST'])
def update_post():
    """Update User"""
    email = request.form.get('email')

    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database
    if not user:  # if a user is found, we want to redirect back to update page so user can try again
        flash('Email address not exists')
        return redirect(url_for('auth.update'))

    user.name = request.form.get('name')
    password = request.form.get('password')
    user.password = generate_password_hash(password, method='sha256')
    user.role = request.form.get('role')

    # update the user to the database
    db.session.add(user)
    db.session.commit()

    flash('User Updated')
    return redirect(url_for('auth.update'))

@auth.route('/logout')
@login_required
def logout():
    """Logout and Redirect to main page"""
    logout_user()
    return redirect(url_for('main.index'))
