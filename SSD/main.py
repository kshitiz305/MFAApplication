"""
main.py
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Index page"""
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    """User profile page (login required)"""
    return render_template('profile.html', name=current_user.name)


@main.route('/upload')
@login_required
def upload():
    """Upload page (login required)"""
    return render_template('upload.html')


@main.route('/download')
@login_required
def download():
    """Download page (login required)"""
    return render_template('download.html')
