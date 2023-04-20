from endpoints_functions.store_api_helpers import Order
import names
import random
import requests


order_endpoint = 'https://petstore.swagger.io/v2/store/order'
inventory_endpoint = 'https://petstore.swagger.io/v2/store/inventory'
store_to_add = Order().create_order()
stored_order_json = []


def add_order_pet():
    added_place = requests.post(url=order_endpoint, json=store_to_add)
    store_json = added_place.json()
    order_id = store_json['id']
    return added_place, str(order_id), store_json


def get_purchase_order_by_id(_id):
    get_order = requests.get(url=order_endpoint + '/' + str(_id))
    return get_order


def add_order_pet_as_maciek():
    added_place = requests.post(url=order_endpoint, json=store_to_add)
    store_json = added_place.json()
    order_id = store_json['id']
    stored_order_json.clear()
    stored_order_json.append(store_json)
    return added_place, str(order_id), store_json


def get_order_by_id_as_maciek():
    order_id = add_order_pet_as_maciek()[1]
    found_order = requests.get(url=order_endpoint + '/' + order_id)
    return found_order


def get_pet_inventory_by_status():
    get_inventory = requests.get(url=inventory_endpoint)
    get_inventory_json = get_inventory.json()
    print('get_inventory_json: ', type(get_inventory_json), get_inventory_json)
    return get_inventory, get_inventory_json

#print(get_pet_inventory_by_status())


def delete_order_by_id(_id):
    delete_order = requests.delete(url=order_endpoint + '/' + str(_id))
    return delete_order




