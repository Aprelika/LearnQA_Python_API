import requests

respons = requests.get("https://playground.learnqa.ru/api/long_redirect")
for r in respons.history:
    print(r.status_code, r.url)
else:
    allow_responses=False
    print("Итоговый редерект: ", r.status_code, r.url)