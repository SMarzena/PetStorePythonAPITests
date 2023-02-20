import requests

request_common_url = "https://petstore.swagger.io/v2/user"
new_user_body = {
    "username": "Mtest",
    "firstName": "Mtest",
    "lastName": "Mtest",
    "email": "mtest@op.com",
    "password": "mtest",
    "phone": "111222333",
    "userStatus": 1
}


## Endpoints functions ##
def post_create_user(user):
    response = requests.post(request_common_url, json=user)
    return response
