from endpoints_functions.store_api_helpers import Order
import names
import random
import requests


endpoint = 'https://petstore.swagger.io/v2/store/order'
store_to_add = Order().create_order()


def add_order_pet():
    added_place = requests.post(url=endpoint, json=store_to_add)
    print('added_place ', added_place)
    store_json = added_place.json()
    order_id = store_json['id']
    return added_place, str(order_id), store_json



