from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional, List
from app.schemas import Book
from app.database import books_db
from app.dependencies import get_current_user

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("", response_model=List[Book])
async def get_books():
    return books_db

@router.get("/search", response_model=List[Book])
async def search_books(author: Optional[str] = None, title: Optional[str] = None):
    results = books_db
    if author:
        results = [b for b in results if author.lower() in b.author.lower()]
    if title:
        results = [b for b in results if title.lower() in b.title.lower()]
    return results

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@router.post("", response_model=Book)
async def create_book(book: Book, current_user: str = Depends(get_current_user)):
    book.id = len(books_db) + 1
    books_db.append(book)
    return book

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book, current_user: str = Depends(get_current_user)):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            updated_book.id = book_id
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@router.delete("/{book_id}")
async def delete_book(book_id: int, current_user: str = Depends(get_current_user)):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return {"detail": f"Book with id {book_id} deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
