import pytest
from app import app

@pytest.fixture
def client():
    """Crea un cliente de prueba para la aplicación Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Prueba la ruta principal"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hola Mundo' in response.data

def test_health_endpoint(client):
    """Prueba el endpoint de health check"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['status'] == 'OK'
    assert 'funcionando correctamente' in data['message']

def test_404_error(client):
    """Prueba que las rutas inexistentes devuelvan 404"""
    response = client.get('/ruta-que-no-existe')
    assert response.status_code == 404