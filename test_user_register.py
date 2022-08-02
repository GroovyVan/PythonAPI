import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def test_create_user_with_exsting_email(selfs):
        email= 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': 'vinkotov@example.com'
        }

        response = requests.post("https://playground.learnqa.ru/apo/user/", data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email} already exist", f"Unexpected response content {response.content}"