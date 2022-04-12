import requests

respons = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(respons.history,)
first_response = respons.history[0]
second_response = respons
print(first_response.url)
print(second_response.url)
print("Итоговый редирект: ", second_response.url)