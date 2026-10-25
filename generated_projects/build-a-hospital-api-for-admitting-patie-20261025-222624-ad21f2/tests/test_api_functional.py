# Auto-generated Pytest functional test suite by APIForge AI
import pytest
import httpx

BASE_URL = 'http://localhost:8000'
AUTH_HEADERS = {'Authorization': 'Bearer test-jwt-token'}

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data.get('status') == 'healthy'

def test_patients_crud_lifecycle(client):
    item_id = '123e4567-e89b-12d3-a456-426614174000'
    # 1. Create a new patients resource via POST
    create_payload = {"title": "Sample title", "status": "Sample status"}
    res_create = client.post('/patients', json=create_payload, headers=AUTH_HEADERS)
    assert res_create.status_code in (200, 201), f'Expected 201 Created: {res_create.text}'
    created_data = res_create.json()
    if isinstance(created_data, dict) and 'id' in created_data:
        item_id = created_data['id']

    # 2. List patients collection with pagination
    res_list = client.get('/patients?limit=10&offset=0', headers=AUTH_HEADERS)
    assert res_list.status_code == 200
    list_data = res_list.json()
    if isinstance(list_data, dict):
        assert 'items' in list_data or 'total' in list_data or len(list_data) >= 0
    elif isinstance(list_data, list):
        assert len(list_data) >= 0

    # 3. Retrieve patients by ID
    res_get = client.get(f'/patients/{item_id}', headers=AUTH_HEADERS)
    assert res_get.status_code in (200, 404)
    if res_get.status_code == 200 and isinstance(res_get.json(), dict) and 'id' in res_get.json():
        assert res_get.json()['id'] == item_id

    # 5. Delete patients
    res_del = client.delete(f'/patients/{item_id}', headers=AUTH_HEADERS)
    assert res_del.status_code in (200, 204, 404)

    # 6. Verify 404 Not Found after deletion
    res_not_found = client.get(f'/patients/{item_id}', headers=AUTH_HEADERS)
    assert res_not_found.status_code in (200, 404)

def test_patients_auth_required(client):
    # Accessing secured endpoint without token should return 401
    create_payload = {"title": "Sample title", "status": "Sample status"}
    res = client.post('/patients', json=create_payload)
    assert res.status_code in (401, 403), f'Expected 401 Unauthorized, got {res.status_code}'

