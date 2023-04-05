from endpoints_functions.useful_stuff import Pet
import names
import random
import requests

endpoint = 'https://petstore.swagger.io/v2/pet'
generated_name = names.get_first_name()
pet_to_add = Pet(name=generated_name).create_pet()
status = random.choice(['available', 'pending', 'sold'])


def add_new_pet():
    added_pet = requests.post(url=endpoint, json=pet_to_add)
    pet_id = added_pet.json()['id']
    pet_name = added_pet.json()['name']
    pet_json = added_pet.json()
    return added_pet, str(pet_id), pet_name, pet_json


def find_pet_by_id():
    pet_id = add_new_pet()[1]
    founded_pet = requests.get(url=endpoint + '/' + pet_id)
    return founded_pet


def find_pet_by_status():
    found_pet_by_status = requests.get(url=endpoint + f"/findByStatus?status={status}")
    return found_pet_by_status


def update_a_pet_with_form_data():
    pet_id = add_new_pet()[1]
    pet_name = names.get_first_name()
    updated_pet = requests.post(url=endpoint + '/' + pet_id, data=f"name={pet_name}&status{status}")
    return updated_pet


def update_an_existing_pet():
    pet_json = add_new_pet()[3]
    pet_json.update({"status": status})
    pet_json.update({"name": names.get_first_name()})
    updated_existing_pet = requests.put(url=endpoint, json=pet_json)
    return updated_existing_pet


def delete_a_pet():
    pet_id = add_new_pet()[1]
    deleted_pet = requests.delete(url=endpoint + '/' + pet_id)
    return deleted_pet

