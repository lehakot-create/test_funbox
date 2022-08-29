import redis

from utils import url_parser
from fastapi.testclient import TestClient
from datetime import datetime

from main import app
from db import RedisConnector

client = TestClient(app)


class TestUrlParser:
    test_cases = [
        ('ya.ru', 'ya.ru'),
        ('yandex.ru', 'yandex.ru/123'),
        ('google.com', 'google.com'),
        ('ya.ru', 'https://ya.ru'),
        ('ya.ru', "https://ya.ru?q=123"),
        ('funbox.ru', "funbox.ru"),
        ("stackoverflow.com", "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor")
    ]

    def test_url_parser(self):
        for el in self.test_cases:
            print(el[0])
            assert [el[0]] == url_parser([el[1]])


def test_post_links():
    url = 'http://127.0.0.1:8000/visited_links'
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
        ]
    }
    response = client.request('POST', url=url, json=data)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_redis_write_links():
    list_url = [
        "ya.ru",
        "funbox.ru",
        "stackoverflow.com"
    ]
    rec_time = str(datetime.now().strftime('%s'))
    conn = RedisConnector()
    conn.write_links(receiving_time=rec_time, list_url=list_url)

    r = redis.StrictRedis(decode_responses=True)
    assert r.lrange(rec_time, 0, -1) == list_url
