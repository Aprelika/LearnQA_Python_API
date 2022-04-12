import requests

class TestCookie:
      def test_cookie(self):
response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
cookie_value = dict(response.cookies) #
for key in cookie_value:
    print(cookie_value[key])
else:
    print(key)
assert "HomeWork" in cookie_value, "These cookies are not in the response"
expected_respose_key = key
expected_respose_value = cookie_value[key]
assert expected_respose_key == expected_respose_value, "Cookies is not correct"