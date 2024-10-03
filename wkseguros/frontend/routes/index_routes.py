from datetime import datetime

from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def login():
    return render_template('app/login.html')


@index_bp.route('/home')
def index():
    current_year = datetime.now().year
    return render_template('site/home.html', current_year=current_year)
