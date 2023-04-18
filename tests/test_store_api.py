from http import HTTPStatus
from endpoints_functions import store_endpoints


def test_add_new_order_verify_status_code():
    """
    Test: Add a new place an order for a pet, check status code
    method: POST
    :return: https://petstore.swagger.io/v2/store/order
    """
    response = store_endpoints.add_order_pet()[0]
    assert response.status_code == HTTPStatus.OK


def test_add_new_order_verify_header():
    """
    Test: Add a new place an order for a pet, check header
    method: POST
    :return: https://petstore.swagger.io/v2/store/order
    """
    response = store_endpoints.add_order_pet()[0]
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'

