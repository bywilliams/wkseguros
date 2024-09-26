from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('site/home.html', current_year=current_year)
