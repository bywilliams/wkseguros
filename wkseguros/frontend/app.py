from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('app/login.html')


@app.route('/home')
def index():
    current_year = datetime.now().year
    return render_template('site/home.html', current_year=current_year)
