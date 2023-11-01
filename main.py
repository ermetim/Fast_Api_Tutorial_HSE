# Реализация эндпоинтов ("ручек")
# !pip install fastapi nest-asyncio pyngrok uvicorn

from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse

app = FastAPI()

"""uvicorn main:app --reload
(запуск веб-сервера с указанием начального скрипта main.py и объекта
FastAPI который создали инструкцией app = FastAPI())
"""


@app.get("/") # Обращение к localhost 127.0.0.1:8000
def root():
    return {"message": "Hello, AI Student!"}
# Запрос http://127.0.0.1:8000

@app.get("/add") # Добавление
def add(x: int, y: int) -> int: # Соответствие типов на входе и выходе важно
    return x + y
# Запрос http://127.0.0.1:8000/add?x=5&y=8


@app.get("/double/{number}")
def double(number: int) -> int:
    return number * 2
# Передача параметров через ручку
# Запрос http://127.0.0.1:8000/double/3


@app.get("/welcome/{name}")
def welcome(name: str = Path(min_length=2, max_length=20)) -> str:
    return f"Good luck, {name}!"


@app.get("/phone/{number}")
def phone_number(number: str = Path(pattern="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")):
    return {"phone": number}


@app.get("/text")
def get_text():
    content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    return PlainTextResponse(content=content)


@app.get("/html")
def get_html():
    content = "<h2>HTML!!!!</h2>"
    return HTMLResponse(content=content)

# ИЛИ

# @app.get("/html", response_class=HTMLResponse)
# def get_html():
#     content = "<h2>HTML!!!!</h2>"
#     return content


@app.get("/file1")
def get_file1():
    content = "index.html"
    return FileResponse(content)
# Возврат содержимого файла

@app.get("/file")
def get_file():
    content = "index.html"
    return FileResponse(
        content,
        media_type="application/octet-stream",
        filename="index_3.html"
    )
# Возврат файла
