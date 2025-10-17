from sqlmodel.ext.asyncio.session import AsyncSession
from service import Marker_model, Marker_Create_model, MarkerUpdate_model
from sqlmodel import select
from models import Marker_model


class BookService:
    async def get_all_bookmarks(self, session: AsyncSession):
        statement = select(Marker_model).order_by(Marker_model.title.asc())
        result = await session.exec(statement)
        return result.scalars().all()

    async def get_book(self, book_uid: str, session: AsyncSession):
        statement = select(Marker_model).where(Marker_model.uid == book_uid)
        result = await session.exec(statement)
        return result.first()
        return book if book is not None else None

    async def create_bookmark(self, book_data: Marker_Create_model, session: AsyncSession):
        book_data_dick = book_data.model_dump()

        new_book = Marker_model(
            **book_data_dick
        )

        session.add(new_book)
        await session.commit()
        return new_book

    async def update_bookmark(self, book_uid: str, update_data: MarkerUpdate_model, session: AsyncSession):
        book_to_update = self.get_book(book_uid, session)
        if book_to_update is not None:
            update_data_dict = update_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)

            await session.commit()
            return book_to_update

    async def delete_bookmark(self, book_uid: str, session: AsyncSession):
        book_to_delete = self.get_book(book_uid, session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            
        else:
            return None
        
        
