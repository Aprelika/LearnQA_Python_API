from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure
@allure.epic("Проверка создания пользователя")
class TestUserRegister(BaseCase):
    @allure.description("Создание пользователя с корректными данными")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Создание пользователя с существующим email")
    def test_create_user_with_existing_email(self):
       email = 'vinkotov@example.com'
       data = self.prepare_registration_data(email)
       response = MyRequests.post("/user/", data=data)
       Assertions.assert_code_status(response, 400)
       assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description("Создание пользователя с некорректным email без @")
    def test_create_user_with_incorrect_mail(self):
        email = 'testmailexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    @allure.description("Создание пользователя. Короткое имя (1 символ)")
    def test_create_user_with_short_name(self):
        username = "l"
        data = self.prepare_registration_data_username(username)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short"

    @allure.description("Создание пользователя. Длинное имя (>260)")
    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data_username()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long"