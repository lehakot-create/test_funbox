### Запустить тесты 
pytest tests.py

### Запустить сервер 
uvicorn main:app --reload

### Описание ендпоинтов 
http://0.0.0.1:8000/docs


### Ендпоинт для учета ссылок:
http://0.0.0.1:8000/visited_links
В теле запроса: {
    "links": [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
} 

### Ендпоинт для статистики 
http://0.0.0.0:8000/visited_domains?from=1661797523&to=1661797781



### Запустить через Docker
docker-compose up --build -d

### Остановить Docker
docker-compsoe stop