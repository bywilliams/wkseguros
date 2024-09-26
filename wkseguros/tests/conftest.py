import pytest

from wkseguros.frontend.app import app  # Importe o app diretamente


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
