from http import HTTPStatus
from unittest.mock import patch

from flask import url_for
from flask.testing import FlaskClient


class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):
        return {
            'id': 1,
            'email': 'test_user@example.com',
            'username': 'test_user',
            'access_level': 1,
        }


def test_login_page(client: FlaskClient):
    """Testa o endpoint / que é a página de login"""
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert 'Login' in response.data.decode('utf-8')


@patch('requests.post')
def test_login(mock_post, client: FlaskClient):
    """Testa o login com email e senha"""

    mock_post.return_value = MockResponse(HTTPStatus.OK)

    response = client.post(
        '/login',
        data={'email': 'test_user@example.com', 'password': 'password123'},
    )
    assert response.status_code == HTTPStatus.FOUND
    # Redirecionamento após o login
    assert response.headers['Location'] == '/dashboard'

    with client.session_transaction() as session:
        assert session['user']['email'] == 'test_user@example.com'


@patch('requests.post')
def test_login_invalid(mock_post, client: FlaskClient):
    """Testa o login com credenciais inválidas"""
    mock_post.return_value = MockResponse(HTTPStatus.UNAUTHORIZED)

    response = client.post(
        '/login',
        data={'email': 'wrong_user@example.com', 'password': 'wrongpassword'},
    )
    assert response.status_code == HTTPStatus.OK
    # Deve retornar a página de login novamente
    assert 'Login' in response.data.decode('utf-8')


def test_dashboard_page(client: FlaskClient):
    """Testa o endpoint /dashboard"""
    with client.session_transaction() as session:
        session['user'] = {
            'email': 'test_user@example.com',
            'password': 'password123',
        }
    response = client.get('/dashboard')
    assert response.status_code == HTTPStatus.OK
    assert 'WK Seguros' in response.data.decode('utf-8')


def test_dashboard_redirect(client: FlaskClient):
    """Testa o redirecionamento do /dashboard para /login se não estiver logado"""
    response = client.get('/dashboard')
    assert (
        response.status_code == HTTPStatus.FOUND
    )  # Verifica se há redirecionamento
    assert response.headers['Location'] == url_for('index.login')


def test_logout(client: FlaskClient):
    """Testa o logout"""
    with client.session_transaction() as session:
        session['user'] = {'email': 'test_user@example.com'}
    response = client.get('/logout')
    assert response.status_code == HTTPStatus.FOUND
    # Redirecionamento após o logout
    assert response.headers['Location'] == url_for('index.login')
    with client.session_transaction() as session:
        assert 'user' not in session
