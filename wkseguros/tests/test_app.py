from datetime import datetime
from http import HTTPStatus


def test_index(client):
    """Testa o endpoint / para garantir
    que a página inicial é renderizada corretamente"""
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert 'Bem-vindo à Página Inicial' in response.data.decode('utf-8')
    current_year = datetime.now().year
    assert str(current_year) in response.data.decode()
