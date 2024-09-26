from http import HTTPStatus


def test_home(client):
    reponse = client.get('/')

    assert reponse.status_code == HTTPStatus.OK
