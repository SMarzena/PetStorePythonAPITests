from endpoints_functions.user_api_helpers import post_create_user, new_user_body


def test_create_user_status_code():
    response = post_create_user(user=new_user_body)
    assert response.status_code == 200


def test_create_user_headers():
    response = post_create_user(user=new_user_body)
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_create_user_url():
    response = post_create_user(user=new_user_body)
    assert response.url == 'https://petstore.swagger.io/v2/user'
