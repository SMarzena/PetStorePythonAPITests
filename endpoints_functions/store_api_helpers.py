from endpoints_functions.general_helpers import generate_id

import random
import datetime


def generate_status_name():
    status_name_list = ['ordered', 'sent', 'placed']
    status_name = random.choice(status_name_list)
    return status_name


def generate_complete_bool():
    complete_bool = bool(random.randint(0, 1))
    return complete_bool


def generate_quantity():
    quantity = random.randint(1, 1000)
    return quantity


def generate_current_date():
    current_date_str = str(datetime.datetime.now())
    modified_date = current_date_str[:10] + 'T' + current_date_str[11:]
    return modified_date


def generate_order_id():
    generated_order_id = random.randint(1, 10)
    return generated_order_id


class Order:
    def __init__(self):
        print('Order object created')

    def create_order(self):
        basic_order = {
            "id": generate_order_id(),
            "petId": generate_id(),
            "quantity": generate_quantity(),
            "shipDate": generate_current_date(),
            "status": generate_status_name(),
            "complete": generate_complete_bool()
        }
        return basic_order
