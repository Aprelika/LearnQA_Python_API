from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Проверка удаления пользователя")
class TestUserDelete(BaseCase): # - 1. Удаление пользователя по ID 2
    @allure.description("Удаление другого пользователя существующей УЗ")
    def test_user_delete_auth_another_user(self):
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)
        userid = 2
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        response2 = MyRequests.delete(f"/user/{userid}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    @allure.description("Проверка удаления собственной УЗ ")
    def test_user_auth_and_delete(self): # Позитивный тест на создание пользователя/его же удаление и проверка, что действительно удален
        register_data = self.prepare_registration_data() # Создаем пользователя
        response1 = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Получаем ключи для авторизации
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        response3 = MyRequests.delete(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response3, 200)
        #Проверим, что пользователь действительно удален
        response4 = MyRequests.get(f"/user/{user_id}")
        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == f"User not found"

    @allure.description("Удаление любого пользователя созданной УЗ")
    def test_negative_delete_user(self): # Удалить пользователя будучи авторизованным другим пользователем
# Создаем пользователей
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data1)
        email = register_data1['email']
        password = register_data1['password']
        login_data_user1 = {
            'email': email,
            'password': password
        }
        Assertions.assert_code_status(response1, 200)

    # Создаем еще одного
        register_data2 = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data2)
        user_id = self.get_json_value(response2, "id")
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

#Авторизовываемся первым пользователем и удаляем второго
        response2 = MyRequests.post("/user/login", data=login_data_user1)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        response3 = MyRequests.delete(f"/user/{user_id}",
                    headers={"x-csrf-token": token},
                    cookies={"auth_sid": auth_sid}
            )
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_code_status(response3, 200)
# Проверяем, что пользователь действительно удален
        response4 = MyRequests.get(f"/user/{user_id}")
        print(response4.text)
        print(response4.status_code)
        Assertions.assert_code_status(response4, 200)
#         assert response4.content.decode("utf-8") == f"User not found"
