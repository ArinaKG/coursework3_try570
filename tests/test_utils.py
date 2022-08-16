import pytest

from utils import get_posts_all, for_views

#список ключей
correct_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count","likes_count","pk"]

class TestUtils:
    def test_for_views(self):
        """
        чисто поржать. Тест на работу теста
        :return:
        """
        assert for_views() == 25, 'Ошибка 25'

    def test_get_posts_all(self):
        """
        Тест на некорректный тип файла
        :return:
        """
        res = get_posts_all()
        assert type(res) == list, 'Некорректный тип файла'

    def test_get_posts_all_isinstans(self):
        """
        Тест на некорректный тип файла
        :return:
        """
        res = get_posts_all()
        assert isinstance(res, list) == True, 'Некорректный тип файла'

    def test_on_keys_in_json(self):
        """
        Тест на корректные ключи
        :return:
        """
        res = get_posts_all()[0]
        result = []
        for x in res.keys():
            result.append(x)
        assert result == correct_keys