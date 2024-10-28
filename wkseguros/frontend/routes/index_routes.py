from datetime import datetime
from http import HTTPStatus
from dotenv import load_dotenv
import os
import requests
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    flash,
    jsonify
)

load_dotenv()

index_bp = Blueprint('index', __name__)

BACKEND_URL = os.getenv('BACKEND_URL')

def validate_client_data(client_data):
    field_names = {
        "born_date": "data de nascimento",
        "last_name": "sobrenome",
        "address": "endereço",
        "name": "nome",
        "phone": "telefone",
        "cpf": "CPF",
        "email": "e-mail"
    }
    for key, value in client_data.items():
        if not value:
            field_name = field_names.get(key)
            return False, f"O campo {field_name} não pode estar vazio."
    return True, ""

@index_bp.route('/')
def app():
    return render_template('site/login.html')


@index_bp.route('/dashboard')
def dashboard():
    if 'user' in session:
        current_year = datetime.now().year
        return render_template('app/home.html', current_year=current_year)
    return redirect(url_for('index.login'))


@index_bp.route('/clients', methods=['GET'])
def clients():
    response = requests.get(f'{BACKEND_URL}clients')
    if response.status_code == HTTPStatus.OK:
        clients = response.json()
        return render_template('app/client.html', clients=clients)
    return "Error fetching clients", response.status_code

@index_bp.route('/client', methods=['POST'])
def create_client():
    client_data = {
        'name': request.form['name'],
        'last_name': request.form['last_name'],
        'cpf': request.form['cpf'],
        'born_date': request.form['born_date'],
        'address': request.form['address'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    valid, message = validate_client_data(client_data)
    if not valid:
        flash(message, 'danger')
        return redirect(url_for('index.clients'))
    
    response_email = requests.get(f'{BACKEND_URL}clients/check_email?email={client_data["email"]}')
    response_cpf = requests.get(f'{BACKEND_URL}clients/check_cpf?cpf={client_data["cpf"]}')
    
    if response_email.status_code == HTTPStatus.OK or response_cpf.status_code == HTTPStatus.OK:
        flash("Erro: E-mail ou CPF já existe no sistema", "danger")
        return redirect(url_for('index.clients'))
    
    response = requests.post(f'{BACKEND_URL}clients', json=client_data)
    if response.status_code == HTTPStatus.OK:
        flash("Cliente criado com sucesso!", "success")
        return redirect(url_for('index.clients'))


@index_bp.route('/client/<int:client_id>', methods=['POST'])
def update_client(client_id):
    client_data = {
        'name': request.form['name'],
        'last_name': request.form['last_name'],
        'cpf': request.form['cpf'],
        'born_date': request.form['born_date'],
        'address': request.form['address'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'updated_at': "2024-10-23 18:00:00"
    }
    
    response = requests.put(f'{BACKEND_URL}clients/{client_id}', json=client_data)
    if response.status_code == HTTPStatus.OK:
        return redirect(url_for('index.clients'))
    return "Error fetching clients", response.status_code


@index_bp.route('/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    response = requests.delete(f'{BACKEND_URL}clients/{client_id}')
    if response.status_code == HTTPStatus.OK:
        return redirect(url_for('index.clients'))
    return "Error fetching clients", response.status_code

@index_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post(
            f'{BACKEND_URL}auth/login',
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
