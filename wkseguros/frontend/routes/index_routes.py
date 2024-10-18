from datetime import datetime
from http import HTTPStatus

import requests
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def app():
    return render_template('site/login.html')


@index_bp.route('/dashboard')
def dashboard():
    if 'user' in session:
        current_year = datetime.now().year
        return render_template('app/home.html', current_year=current_year)
    return redirect(url_for('index.login'))


@index_bp.route('/clientes')
def clients():
    response = requests.get('http://127.0.0.1:8000/api/v1/clients')
    if response.status_code == HTTPStatus.OK:
        clients = response.json()
        return render_template('app/client.html', clients=clients)
    return "Error fetching clients", response.status_code

@index_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post(
            'http://127.0.0.1:8000/api/v1/auth/login',
            json={'email': email, 'password': password},
        )

        if response.status_code == HTTPStatus.OK:
            session['user'] = response.json()
            return redirect('/dashboard')

    return render_template('site/login.html')


@index_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')
