import requests

class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Введите любую фразу: ")
        expected = 15
        assert len(phrase) <= expected, "Ошибка фраза больше 15 символов"