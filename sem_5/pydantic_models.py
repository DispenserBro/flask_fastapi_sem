from pydantic import BaseModel


# Создайте класс Task с полями id, title, description и status.
class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: bool = False


# Создайте класс Movie с полями id, title, description и genre.
class Movie(BaseModel):
    id: int
    title: str
    description: str | None = None
    genre: str