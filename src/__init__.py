from fastapi import FastAPI
from src.books.routes import book_router
from src.books.routes import book_router 

version = "v1"
app = FastAPI(
    title="Bookmarks API",
    version=version
)

app.include_router(
    book_router, prefix=f"/api/{version}/bookmarker", tags=["bookmarks"])
