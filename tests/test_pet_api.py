from http import HTTPStatus
from endpoints_functions import pet_endpoints


def test_add_a_new_pet_status_code():
    """
    Test: Add a new pet to the store, check status code
    method: POST
    endpoint: https://petstore.swagger.io/v2/pet
    """
    response = pet_endpoints.add_new_pet()[0]
    assert response.status_code == HTTPStatus.OK


def test_add_a_new_pet_header():
    """
    Test: Add a new pet to the store, check header
    method: POST
    endpoint: https://petstore.swagger.io/v2/pet
    """
    response = pet_endpoints.add_new_pet()[0]
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_finding_pet():
    """
    Test: Find pet by ID
    method: GET
    endpoint: https://petstore.swagger.io/v2/pet/{id}
    """
    response = pet_endpoints.find_pet_by_id()
    assert response.status_code == HTTPStatus.OK


def test_finding_pet_by_status_status_code():
    """
    Test: Find pet by status, check status code
    method: GET
    endpoint: https://petstore.swagger.io/v2/pet/findByStatus
    """
    response = pet_endpoints.find_pet_by_status()
    assert response.status_code == HTTPStatus.OK


def test_finding_pet_by_status_url():
    """
    Test: Find pet by status, check url contains 'findByStatus'
    method: GET
    endpoint: https://petstore.swagger.io/v2/pet/findByStatus
    """
    response = pet_endpoints.find_pet_by_status()
    assert '/findByStatus?status=' in response.url


def test_update_a_pet_with_form_data_status_code():
    """
    Test: Update a pet in the store with form data, check status code
    method: POST
    endpoint: https://petstore.swagger.io/v2/pet/{id}
    """
    response = pet_endpoints.update_a_pet_with_form_data()
    assert response.status_code == HTTPStatus.OK


def test_update_a_pet_with_form_data_check_message():
    """
    Test: Update a pet in the store with form data, check if message is equal to pet id
    method: POST
    endpoint: https://petstore.swagger.io/v2/pet/{id}
    """
    original_pet = pet_endpoints.add_new_pet()[1]
    updated_pet = pet_endpoints.update_a_pet_with_form_data()
    assert updated_pet.json()["message"] == original_pet


def test_update_an_existing_pet_status_code():
    """
    Test: Update an existing pet in the store, check status code
    method: PUT
    endpoint: https://petstore.swagger.io/v2/pet/
    """
    response = pet_endpoints.update_an_existing_pet()
    assert response.status_code == HTTPStatus.OK


def test_update_an_existing_pet_compare_names():
    """
    Test: Update an existing pet in the store, check if name is changed
    method: PUT
    endpoint: https://petstore.swagger.io/v2/pet/
    """
    original_pet = pet_endpoints.add_new_pet()[2]
    updated_pet = pet_endpoints.update_an_existing_pet()
    assert updated_pet.json()["name"] != original_pet


def test_delete_pet():
    """
    Test: Delete a pet, check status code
    method: DELETE
    endpoint: https://petstore.swagger.io/v2/pet/{id}
    """
    deleted_pet = pet_endpoints.delete_a_pet()
    assert deleted_pet.status_code == HTTPStatus.OK


def test_delete_pet_compare_id():
    """
    Test: Delete a pet, check if message is equal to pet id
    method: DELETE
    endpoint: https://petstore.swagger.io/v2/pet/{id}
    """
    original_pet = pet_endpoints.add_new_pet()[1]
    deleted_pet = pet_endpoints.delete_a_pet()
    assert deleted_pet.json()["message"] == original_pet
