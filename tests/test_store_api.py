from http import HTTPStatus
from endpoints_functions import store_endpoints
from pathlib import Path
import pytest


def test_add_new_order_verify_status_code():
    """
    Test: Add a new place an order for a pet, check status code
    method: POST
    endpoint: https://petstore.swagger.io/v2/store/order
    """
    response = store_endpoints.add_order_pet()[0]
    assert response.status_code == HTTPStatus.OK


def test_add_new_order_verify_header():
    """
    Test: Add a new place an order for a pet, check header
    method: POST
    endpoint: https://petstore.swagger.io/v2/store/order
    """
    response = store_endpoints.add_order_pet()[0]
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_add_new_order_verify_json_by_ge_endpoint():
    """
    Test: Add a new place an order for a pet, compare received json with received by get endpoint
    Separate those endpoints is good solution if we want to GET id which is already in DB.
    methods: POST, GET
    endpoint: https://petstore.swagger.io/v2/store/order
    endpoint: https://petstore.swagger.io/v2/store/order/{id}
    """
    post_response = store_endpoints.add_order_pet()[2]
    response_id = post_response['id']
    get_response = store_endpoints.get_purchase_order_by_id(response_id)
    assert post_response == get_response.json()


# Same test case but by Maciek's way
def test_add_new_order_to_temp_list_verify_json():
    """
    Test: Add new place an order for a pet to temp list - this endpoint is inside function get_order_by_id_as_maciek.
    Compare with json received by GET
    methods: POST and GET
    endpoint: https://petstore.swagger.io/v2/store/order
    endpoint: https://petstore.swagger.io/v2/store/order/{id}
    """
    stored_order_json = store_endpoints.stored_order_json
    order_by_id = store_endpoints.get_order_by_id_as_maciek()
    assert stored_order_json[0] == order_by_id.json()


@pytest.mark.skip
def test_get_order_from_db_compare_json_with_expected_file():
    """
    Test: Get order already exists in DB
    method: GET
    endpoint: https://petstore.swagger.io/v2/store/order/{id}
    !!Test is not stable because there is no access to pet store DB and order id is changing often.
    !!This is a reason of skip test
    """
    get_response_json = str(store_endpoints.get_purchase_order_by_id(6).json())
    file_path = Path("../expected_files/get_order_id_6.json")
    with open(file_path) as file:
        expected_output = file.read()
    # TODO: test passing this way but I can't format json file. It looks ugly. Maybe I should use methods from json library?
    assert get_response_json == expected_output


# def test_get_inventory_verify_json():
#     """
#     Test: Returns a map of status codes to quantities
#     method: GET
#     endpoint: https://petstore.swagger.io/v2/store/inventory
#     """
#     get_response_json = store_endpoints.get_pet_inventory_by_status()[1]
# #    print('get_response_json: ', type(get_response_json), get_response_json)
#     file_path = Path("../expected_files/get_inventory_available.json")
#     with open(file_path) as file:
#         expected_output = file.read()
#         print('exp', type(expected_output))
#         expected_output_dict = dict(expected_output)
#         print('dict', type(expected_output_dict))
# TODO inside with modify file to change string and available value because they ae random. Add 'skip' there
# print('expected_output_dict: ', type(expected_output_dict), expected_output_dict)
# expected_output['available'] = 'skipped'
# print('expected_output: ', expected_output)
#    assert get_response_json == expected_output_440


def test_delete_order_verify_status_code():
    """
    Test: Add a new order for a pet, get id for created order, use it for delete order
    methods: POST, DELETE
    endpoint: https://petstore.swagger.io/v2/store/order
    endpoint: https://petstore.swagger.io/v2/store/order/{id}
    """
    post_response = store_endpoints.add_order_pet()[2]
    response_id = post_response['id']
    delete_response = store_endpoints.delete_order_by_id(response_id)
    assert delete_response.status_code == HTTPStatus.OK
