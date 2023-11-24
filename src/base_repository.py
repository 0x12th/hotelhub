from typing import Any, Generic, TypeVar

from sqlalchemy import RowMapping, insert, select

from src.db import async_session_maker

_T = TypeVar("_T")


class BaseRepository(Generic[_T]):
    model: type[_T]

    @classmethod
    async def get_one_or_none(cls, **params: Any | None) -> Any | None:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **params: Any | None) -> Any | list[Any]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **data: Any | None) -> RowMapping | None:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one_or_none()
