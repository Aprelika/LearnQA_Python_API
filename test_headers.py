import requests

class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(dict(response.headers))
        header_key = "x-secret-homework-header"
        header_value = response.headers.get("x-secret-homework-header")
        print(header_value)
        headers = {"x-secret-homework-header": header_value}
        header_value = 'Some secret value'
        print(headers)

        assert header_key in response.headers, "Неaders 'x-secret-homework-header' not found in the responce"
        assert header_value == 'Some secret value', "There is not value 'Some secret value' in the header 'x-secret-homework-header'"