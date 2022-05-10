import pytest
import requests

class TestUserAgent:
    some_value_here = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]
    expected_value = [
        ("'platform': 'Mobile', 'browser': 'No', 'device': 'Android'"),
        ("'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'"),
        ("'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'"),
        ("'platform': 'Web', 'browser': 'Chrome', 'device': 'No'"),
        ("'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'")
    ]

    @pytest.mark.parametrize('some_value_here', some_value_here, 'expected_value', expected_value)
    def test_user_agent(self, some_value_here, expected_value):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {'User-Agent': some_value_here}
        response = requests.get(url, headers=headers)
        response_dict = response.json()
        header_key = response.request.headers['User-Agent']
        user_agent = response.json()['user_agent']
        platform = response.json()['platform']
        browser = response.json()['browser']
        device = response.json()['device']

        expected_response_text = f"'platform': '{platform}', 'browser': '{browser}', 'device': '{device}'"
        # assert response.status_code == 200, "Wrong response code"
        # assert header_key == user_agent, "There is not value 'user_agent' in the response"
        assert 'user_agent' in response_dict, "There is not field 'user_agent' in the response"
        assert 'platform' in response_dict, "There is not field 'platform' in the response"
        assert 'browser' in response_dict, "There is not field 'browser' in the response"
        assert 'device' in response_dict, "There is not field 'device' in the response"
        assert expected_response_text in expected_value, "Полученное значение" f"'{expected_response_text}' не найдено в '{expected_value}'"