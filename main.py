from fastapi import FastAPI, Request
from datetime import datetime

from models import Links
from utils import url_parser
from db import RedisConnector

app = FastAPI()
conn = RedisConnector()


@app.post('/visited_links')
async def post_links(links: Links):
    """
    Получает и сохраняет ссылки в БД
    """
    receiving_time = datetime.now().strftime('%s')
    result = url_parser(links.links)
    conn.write_links(receiving_time=receiving_time, list_url=result)
    return {"status": "ok"}


@app.get('/visited_domains')
async def get_static(request: Request):
    """
    Возвращает список посещенных доменов за период
    """
    params = request.query_params
    dct = {"from": params.get('from'),
           "to": params.get('to')}
    if dct['from'] is None:
        return {'status': 'error',
                "descriptions": "отсутствует параметр 'from'"}

    if dct['to'] is None:
        return {'status': 'error',
                "descriptions": "отсутствует параметр 'to'"}
    list_visited_domains = set(conn.get_links(dct))
    return {
        "domains": list_visited_domains,
        "status": "ok"
    }
