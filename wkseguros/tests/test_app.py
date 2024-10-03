from datetime import datetime
from http import HTTPStatus


def test_login(client):
    """Testa o endpoint / par que é a página de login"""
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert '2024 WK Seguros.' in response.data.decode('utf-8')


def test_home(client):
    """Testa o endpoint /home para garantir
    que a página de dashboard é renderizada corretamente"""
    response = client.get('/home')

    assert response.status_code == HTTPStatus.OK
    assert 'Bem-vindo à WK Seguros' in response.data.decode('utf-8')
    current_year = datetime.now().year
    assert str(current_year) in response.data.decode()
