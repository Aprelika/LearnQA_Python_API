import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestNegativeEditUser(BaseCase):
    def test_put_user_not_auth(self):
# Создание пользователя для редактирования
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id = self.get_json_value(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
 #Редактируем созданного пользователя без авторизации
        new_email = 'asdsdfsdfds@example.com'
        response2 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}", data={"email": new_email})

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == f"Auth token not supplied"
#Измененяем данные пользователя с авторизацией другого пользователя
    def test_put_edit_user_auth_another(self):
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        name = 'TestTes'
        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/225",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": name}
        )
        Assertions.assert_code_status(response2, 400) # Вот тут честно не понимаю, user_id > 10, а ошибка, что нельзя редактировать до ID 5
        assert response2.content.decode("utf-8") == f"Please, do not edit test users with ID 1, 2, 3, 4 or 5."

        # Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
    def test_put_edit_user_email(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")
        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        # EDIT
        email = 'testmailexample.com'
        edit_data = self.prepare_registration_data(email)
        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=edit_data
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == f"Invalid email format"

        lastName = 'l'
        edit_data_last_name = self.prepare_registration_data_last_name(lastName)
        response4 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=edit_data_last_name
        )
        Assertions.assert_code_status(response4, 400)
        Assertions.assert_json_has_key(response4, "error"), f"Actual: {response4.text}"
