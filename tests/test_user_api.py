from endpoints_functions.user_api_helpers import post_create_user, new_user_body, get_login_user_into_system, get_logout_user_from_current_session
from http import HTTPStatus
import pytest


correct_credentials = {
    "username": 'Mtest',
    "password": 'mtest'
}


def test_create_user_status_code():
    response = post_create_user(user=new_user_body)
    assert response.status_code == HTTPStatus.OK


def test_create_user_headers():
    response = post_create_user(user=new_user_body)
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_create_user_url():
    response = post_create_user(user=new_user_body)
    assert response.url == 'https://petstore.swagger.io/v2/user'


#TODO Ask Maciej about this test - it's not working
#TODO I added import pytest because of this @pytest.mark.skip
@pytest.mark.skip
def test_response_request_user_url():
    response = post_create_user(user=new_user_body)
    assert response.request['POST'] == 'POST'


#TODO Ask Maciej which one is worth to verify in tests?
@pytest.mark.skip
def test____user():
    response = post_create_user(user=new_user_body)
    print("response.json", response.json())
    print(response.json()["message"])
    print("response.text", response.text)
    print("response.content", response.content)
    print("response.request", response.request)
    print("response.cookies", response.cookies)
    print("response.elapsed", response.elapsed)
    print("response.apparent_encoding", response.apparent_encoding)
    print("response.encoding", response.encoding)
    print("response.reason", response.reason)
    print("response.history", response.history)


#### Login user into system
def test_login_user_sucessfull_status_code():
    response = get_login_user_into_system(correct_credentials.get('username'), correct_credentials.get('password'))
    assert response.status_code == HTTPStatus.OK


def test_login_user_headers():
    response = get_login_user_into_system(correct_credentials.get('username'), correct_credentials.get('password'))
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_login_user_correct_url():
    response = get_login_user_into_system(correct_credentials.get('username'), correct_credentials.get('password'))
    assert response.url == f"https://petstore.swagger.io/v2/user/login?username={correct_credentials.get('username')}&password={correct_credentials.get('password')}"


#TODO how to validate data from json when e.g. some information are random? like message
def test_print_response():
    response = get_login_user_into_system(correct_credentials.get('username'), correct_credentials.get('password'))
#    print("response", response)
#    print(response.json()["message"])
    print(response.json())


### Logout user from session
def test_logout_user_from_session_status_code():
    response = get_logout_user_from_current_session()
    assert response.status_code == HTTPStatus.OK


def test_logout_user_from_session_headers():
    response = get_logout_user_from_current_session()
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_logout_user_from_session_correct_url():
    response = get_logout_user_from_current_session()
    assert response.url == "https://petstore.swagger.io/v2/user/logout"


def test_logout_user_from_session_message():
    response = get_logout_user_from_current_session()
#    print("response", response.json())
    assert response.json()["message"] == "ok"


#TODO ask about negative tests e.g verify status code 404. Where is possible to add them? In which endpoint?




