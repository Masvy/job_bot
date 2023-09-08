from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func

from database.create_table import User


async def number_applicants(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(func.count()).where(User.status == 'Соискатель'))
            applicants = result.scalar()
            return applicants


async def applicants_user_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_name).where(User.status == 'Соискатель'))
            user_name = [row[0] for row in result]
            return user_name


async def applicants_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.name).where(User.status == 'Соискатель'))
            names = [row[0] for row in result]
            return names


async def applicants_city(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.city).where(User.status == 'Соискатель'))
            citys = [row[0] for row in result]
            return citys


async def applicants_vacancies(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.vacancies).where(User.status == 'Соискатель'))
            vacancies = [row[0] for row in result]
            return vacancies


async def applicants_employment(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.employment).where(User.status == 'Соискатель'))
            employment = [row[0] for row in result]
            return employment


async def applicants_schedule(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.schedule).where(User.status == 'Соискатель'))
            schedule = [row[0] for row in result]
            return schedule


async def applicants_id(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_id).where(User.status == 'Соискатель'))
            user_id = [row[0] for row in result]
            return user_id


async def number_satisfied(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(func.count()).where(User.status == 'Устраивает'))
            applicants = result.scalar()
            return applicants


async def satisfied_user_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_name).where(User.status == 'Устраивает'))
            user_name = [row[0] for row in result]
            return user_name


async def satisfied_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.name).where(User.status == 'Устраивает'))
            names = [row[0] for row in result]
            return names


async def satisfied_city(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.city).where(User.status == 'Устраивает'))
            citys = [row[0] for row in result]
            return citys


async def satisfied_vacancies(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.vacancies).where(User.status == 'Устраивает'))
            vacancies = [row[0] for row in result]
            return vacancies


async def satisfied_employment(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.employment).where(User.status == 'Устраивает'))
            employment = [row[0] for row in result]
            return employment


async def satisfied_schedule(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.schedule).where(User.status == 'Устраивает'))
            schedule = [row[0] for row in result]
            return schedule


async def satisfied_id(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_id).where(User.status == 'Устраивает'))
            user_id = [row[0] for row in result]
            return user_id
