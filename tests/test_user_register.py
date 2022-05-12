import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import random
import string

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.username = random_name = ''.join(random.choices(string.ascii_letters, k=260))
    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
       email = 'vinkotov@example.com'
       data = {
           'password': '123',
            'username': 'learnqa',
           'firstName': 'learnqa',
           'lastName': 'learnqa',
           'email': email
       }
       response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
       Assertions.assert_code_status(response, 400)
       assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_mail(self):
        email = 'testmailexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    def test_creat_user_with_short_name(self):
        data = {
            'password': '123',
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short"

    def test_create_user_with_long_name(self):
        data = {
            'password': '123',
            'username': self.username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long"