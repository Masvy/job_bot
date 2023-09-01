from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update

from database.create_table import User


async def read_access(user_id, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.access).where(User.user_id == user_id))
            access = result.scalar()
    return access


async def update_access(user_id, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(access=1))


async def update_name(user_id, name, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(name=name))


async def update_city(user_id, city, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(city=city))


async def update_vacancies(user_id, vacancies, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(vacancies=vacancies))


async def update_employment(user_id, employment, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(employment=employment))


async def update_schedule(user_id, schedule, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(schedule=schedule))


async def update_status(user_id, status, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.user_id == user_id).values(status=status))


async def read_data(user_id, session_maker: sessionmaker):
    _session_maker: sessionmaker = session_maker
    async with _session_maker() as session:
        async with session.begin():
            name = await session.execute(select(User.name).where(User.user_id == user_id))
            city = await session.execute(select(User.city).where(User.user_id == user_id))
            vacancies = await session.execute(select(User.vacancies).where(User.user_id == user_id))
            employment = await session.execute(select(User.employment).where(User.user_id == user_id))
            schedule = await session.execute(select(User.schedule).where(User.user_id == user_id))
    return {
        'name': name.scalar(), 'city': city.scalar(),
        'vacancies': vacancies.scalar(), 'employment': employment.scalar(),
        'schedule': schedule.scalar()
        }
