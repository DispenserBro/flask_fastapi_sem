from pydantic import BaseModel


# модель User со следующими полями:
# id: int (идентификатор пользователя, генерируется автоматически)
# username: str (имя пользователя)
# email: str (электронная почта пользователя)
# password: str (пароль пользователя)
class UserOnRegister(BaseModel):
    username: str
    email: str
    password: str


class User(UserOnRegister):
    id: int