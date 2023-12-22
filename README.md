# Задания с семинаров по Flask и FastAPI

Содержание:

- [Описание](#описание)
- [Настройка виртуального окружения](#настройка-виртуального-окружения)
- [Запуск скриптов](#запуск-скриптов)
- [Список семинаров](#список-семинаров)

## Описание

В этом репозитории находятся решения заданий с семинаров  по Flask и FastAPI.

Задания распределены по правилу: `sem_<номер_семинара>/task<номер_задания>.py`.

Все модули отформатированы инструментом [Ruff](https://docs.astral.sh/ruff/) по настройкам в [ruff.toml](./ruff.toml)

В некоторых модулях представлены результаты выполнения сразу нескольких заданий.

Различить из можно по количеству отделённых друг от друга блоков комментариев с заданиями.

Например, в модуле с такими комментариями:

```python
# Написать функцию, которая будет принимать
# на вход два числа и выводить на экран их сумму.
```

Содержится решение только одного задания.

А в модуле с такими комментариями:

```python
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".

# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about" и страницу "contact".
```

Содержится решение двух заданий.

В списке семинаров также будут указываться задания, которые оставили на дом, т.е. их решения не будут появляться в этом репозитории.

## Настройка виртуального окружения

Для настройки виртуального окружения используйте команду 

`py -m venv <название_виртуального_окружения>`

(`python -m venv <название_виртуального_окружения>` на Windows или `python3 -m venv <название_виртуального_окружения>` на Linux, если основная команда не работает)

После этого, активируйте виртуальное окружение командой для вашей ОС.

Для установки необходимых зависимостей, при активном виртуальном окружении выполните команду

`pip install -r requirements.txt`

[Список зависимостей](./requirements.txt):

| Библиотека | Версия |
|---|---|
| Flask | >=3.0.0 |
| ruff | >=0.1.7 |
| Faker | >=20.1.0 |
| Flask-SQLAlchemy | >=3.1.1 |
| Flask-WTF | >=1.2.1 |
| requests | >=2.31.0 |
| aiohttp | >=3.9.1 |
| aiofiles | >=23.2.1 |
| fastapi | >=0.105.0 |
| uvicorn | >=0.25.0 |

Виртуальное окружение настроено!

## Запуск скриптов

Для запуска необходимого скрипта можно использовать три способа:

1. Запустить необходимый скрипт из директории, в которой он находится командой `py <файл>` (`python <файл>` на Windows или `python3 <файл>` на Linux, если основная команда не работает).
2. Изменить первую строку файла [wsgi.py](./wsgi.py) на необходимый пакет и модуль, из которых будет импортироваться переменная `app`, и выполнить команду `flask run` для Flask, которая запускает сервер Flask.
3. ТОЛЬКО ДЛЯ FastAPI: изменить содержимое первого аргумента в 5 строке файла [uvicorn_server.py](./uvicorn_server.py) на строку по шаблону: `<папка_семинара>.<модуль>:app` и выполнить его комадой `py uvicorn_server.py` или аналогичной для вашей ОС.


## Список семинаров

- [Семинар 1](./sem_1/) ДЗ: Задания 7 и 9
- [Семинар 2](./sem_2/) ДЗ: Задания 6 - 9 (сделать как минимум 2)
- [Семинар 3](./sem_3/) ДЗ: Задания 3 - 8 (сделать как минимум 2)
- [Семинар 4](./sem_4/) ДЗ: Задания 7 - 9 (сделать как минимум 7 задачу)
