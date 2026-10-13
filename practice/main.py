from fastapi import FastAPI
from app.middleware import log_requests
from app.routers import auth, books

app = FastAPI(title="Book API Documentation")

app.middleware("http")(log_requests)

app.include_router(auth.router)
app.include_router(books.router)
