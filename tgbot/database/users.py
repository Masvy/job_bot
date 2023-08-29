from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update

from database.create_table import User


async def read_status(user_id, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.status).where(User.user_id == user_id))
            status = result.scalar()
    return status


async def update_status(user_id, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(status=1))
