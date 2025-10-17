from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List

from .marker_data import bookmarks
from .schemas import Marker_model, BookMarkerUpdate_model


book_router = APIRouter()


@book_router.get("/", response_model=List[Marker_model])
async def get_bookmarks():
    return bookmarks


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_bookmark(book_data: Marker_model) -> dict:
    new_bookmark = book_data.model_dump()
    bookmarks.append(new_bookmark)
    return {"message": "Bookmark created successfully", "bookmark": new_bookmark}


@book_router.get("/{id}", response_model=Marker_model)
async def find_bookmark(id: int) -> dict:
    for bookmark in bookmarks:
        if bookmark["id"] == id:
            return bookmark

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Bookmark with id {id} not found"
    )


@book_router.patch("/{id}", response_model=Marker_model)
async def update_bookmark(id: int, book_update_data: BookMarkerUpdate_model) -> dict:
    for index, bookmark in enumerate(bookmarks):
        if bookmark["id"] == id:
            updated_data = book_update_data.model_dump(exclude_unset=True)
            bookmarks[index].update(updated_data)
            return bookmarks[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Bookmark with id {id} not found to update")


@book_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bookmark(id: int):
    for index, bookmark in enumerate(bookmarks):
        if bookmark["id"] == id:
            bookmarks.pop(index)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Bookmark with id {id} not found to delete")
