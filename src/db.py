from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from config import settings

engine = create_async_engine(url=str(settings.POSTGRES_DSN), echo=settings.DB_ECHO)

async_session_maker = async_sessionmaker(
    bind=engine, autoflush=False, expire_on_commit=False
)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:  # noqa: N805
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
