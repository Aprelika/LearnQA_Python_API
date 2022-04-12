import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text, response.status_code)
payload = json.loads(response.text)

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
print(response2.text, response.status_code)

time.sleep(8)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
print(response3.text, response.status_code)