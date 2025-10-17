from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Config

engine = create_async_engine(
    Config.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
    echo=True
)


async def init_db():

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database initialized.")


async def get_session() -> AsyncSession: # type: ignore
    Session = sessionmaker(
        bind=create_async_engine,
        class_=AsyncSession,
        expire_on_commit=False)
    async with Session() as session:
        yield session
