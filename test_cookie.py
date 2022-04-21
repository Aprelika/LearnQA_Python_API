import requests

class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))
        cookie_value = response.cookies.get('HomeWork')
        cookies = {'HomeWork': cookie_value}
        print(cookies)
        cookie_key = "HomeWork"
        cookie_value = "hw_value"
        assert cookie_key in response.cookies, "There is not key 'HomeWork' in the cookie"
        assert cookies[cookie_key] == cookie_value, "There is not value 'hw_value' in the cookie"