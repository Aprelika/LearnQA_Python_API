import requests
#1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print('1. Результат запроса любого типа (GET) без параметра method: {} Статус код: {}'.format(response.text, response.status_code))
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
#2
print("2. http - Отправка типа запроса не из списка (HEAD) без параметров: пустой ответ {}, Статус код {}".format(response.text, response.status_code))
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print("2.1. http - Отправка типа запроса не из списка (HEAD) c параметрами: пустой ответ {}, Статус код {}".format(response.text, response.status_code))
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
#3
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PUT"})
print("3. Запрос PUT с правильным значением method/data. Ответ: {} - Успешно. Статус код {}".format(response.text, response.status_code))
# 4 Сдаюсь(
param =[{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
for key in param:
        print(key)
        result = requests.get(url, params=key)
        print( 'Запрос с params {} в reguest.get , Получем системное сообщение: {}. Статус код {}'.format(key,result.text,result.status_code))
        result = requests.post(url, params=key)
        print('Запрос с params {} в reguest.post , Получем системное сообщение: {}. Статус код {}'.format(key,result.text,result.status_code))
        result = requests.put(url, params=key)
        print('Запрос с params {} в reguest.put , Получем системное сообщение: {}. Статус код {}'.format(key,result.text,result.status_code))
        result = requests.delete(url, params=key)
        print('Запрос с params {} в reguest.delete , Получем системное сообщение: {}. Статус код {}'.format(key,result.text,result.status_code))
        result = requests.get(url, data=key)
        print('Запрос с data {} в reguest.get , Получем системное сообщение: {}. Статус код {}'.format(key, result.text, result.status_code))
        result = requests.post(url, data=key)
        print('Запрос с data {} в reguest.post , Получем системное сообщение: {}. Статус код {}'.format(key, result.text, result.status_code))
        result = requests.put(url, data=key)
        print('Запрос с data {} в reguest.put , Получем системное сообщение: {}. Статус код {}'.format(key, result.text, result.status_code))
        result = requests.delete(url, data=key)
        print('Запрос с data {} в reguest.delete , Получем системное сообщение: {}. Статус код {}'.format(key, result.text, result.status_code))
