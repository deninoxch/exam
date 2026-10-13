from typing import List
from app.schemas import Book

books_db: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", year=1949, isbn="978-0451524935")
]
