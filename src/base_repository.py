from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy import RowMapping, insert, select

from db import async_session_maker

_T = TypeVar("_T")


class BaseRepository(Generic[_T]):
    model: Type[_T]

    @classmethod
    async def get_one_or_none(cls, **params: Optional[Any]) -> Optional[Any]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **params: Optional[Any]) -> Any | list[Any]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **data: Optional[Any]) -> Optional[RowMapping]:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one_or_none()
