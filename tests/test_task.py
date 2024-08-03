# tests/test_task.py

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_task(client):
    response = client.get('/task/1')
    assert response.status_code == 404

def test_create_task(client):
    response = client.post('/task', json={'title': 'Test Task', 'description': 'Test Description'})
    assert response.status_code == 201

def test_update_task(client):
    response = client.post('/task', json={'title': 'Test Task', 'description': 'Test Description'})
    task_id = response.get_json()['id']
    response = client.put(f'/task/{task_id}', json={'title': 'Updated Task'})
    assert response.status_code == 200

def test_delete_task(client):
    response = client.post('/task', json={'title': 'Test Task', 'description': 'Test Description'})
    task_id = response.get_json()['id']
    response = client.delete(f'/task/{task_id}')
    assert response.status_code == 204
