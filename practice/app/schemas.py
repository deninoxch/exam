from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int
    isbn: str
    available: bool = True

class User(BaseModel):
    username: str
    password: str
