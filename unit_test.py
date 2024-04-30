from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Flask App' in response.data  # Adjust this based on your index.html content

def test_index_route_post_valid_credentials(client):
    data = {'name': 'andrew', 'password': '0000'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Logged In Successfully' in response.data  # Adjust this based on your loged_in.html content

def test_index_route_post_invalid_credentials(client):
    data = {'name': 'adada', 'password': 'adad'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'user not found please try again' in response.data  # Adjust this based on your expected error message
