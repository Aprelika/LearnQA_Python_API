import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_create_user(self):
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
        new_name = "Change name"
        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
             headers={"x-csrf-token": token},
             cookies={"auth_sid": auth_sid},
             data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

# Негативные тесты на PUT
    def test_put_user_not_auth(self):
# Создание пользователя для редактирования
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id = self.get_json_value(response1, "id")
 #Редактируем пользователя без авторизации
        new_email = 'asdsdfsdfds@example.com'
        response2 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}", data={"email": new_email})

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == f"Auth token not supplied"
# Измененяем данные пользователя с авторизацией другого пользователя
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        print(email,first_name,password,user_id)
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
        new_name = "dfsdfsdfsdfdfrgf"

        response4 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        print(response4.status_code)
        print(response4.content)
        #
        # response5 = requests.get(
        #     f"https://playground.learnqa.ru/api/user/2",
        #     headers={"x-csrf-token": token},
        #     cookies={"auth_sid": auth_sid}
        #     )
        # print(response2, "firstName")
        # # Assertions.assert_json_value_by_name(
        #     response5,
        #     "firstName",
        #     new_name,
        #     "Wrong name of the user after edit"
        # )
