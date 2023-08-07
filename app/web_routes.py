from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    return render_template('login.html')

@web_bp.route('/admin')
def about():
    return render_template('admin.html')
