import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
print(response.text, response.status_code)
print(response.cookies)