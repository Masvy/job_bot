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
            cities = [row[0] for row in result]
            return cities


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


async def applicants_age(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.age).where(User.status == 'Соискатель'))
            age = [row[0] for row in result]
            return age


async def applicants_experience(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.experience).where(User.status == 'Соискатель'))
            experience = [row[0] for row in result]
            return experience


async def applicants_education(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.education).where(User.status == 'Соискатель'))
            education = [row[0] for row in result]
            return education


async def applicants_question(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.question).where(User.status == 'Соискатель'))
            question = [row[0] for row in result]
            return question


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
            cities = [row[0] for row in result]
            return cities


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


async def satisfied_age(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.age).where(User.status == 'Устраивает'))
            age = [row[0] for row in result]
            return age


async def satisfied_experience(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.experience).where(User.status == 'Устраивает'))
            experience = [row[0] for row in result]
            return experience


async def satisfied_education(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.education).where(User.status == 'Устраивает'))
            education = [row[0] for row in result]
            return education


async def satisfied_id(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_id).where(User.status == 'Устраивает'))
            user_id = [row[0] for row in result]
            return user_id


async def number_leads(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(func.count()).where(User.status == 'Лид'))
            applicants = result.scalar()
            return applicants


async def leads_user_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_name).where(User.status == 'Лид'))
            user_name = [row[0] for row in result]
            return user_name


async def leads_name(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.name).where(User.status == 'Лид'))
            names = [row[0] for row in result]
            return names


async def leads_city(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.city).where(User.status == 'Лид'))
            cities = [row[0] for row in result]
            return cities


async def leads_vacancies(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.vacancies).where(User.status == 'Лид'))
            vacancies = [row[0] for row in result]
            return vacancies


async def leads_employment(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.employment).where(User.status == 'Лид'))
            employment = [row[0] for row in result]
            return employment


async def leads_schedule(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.schedule).where(User.status == 'Лид'))
            schedule = [row[0] for row in result]
            return schedule


async def leads_age(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.age).where(User.status == 'Лид'))
            age = [row[0] for row in result]
            return age


async def leads_experience(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.experience).where(User.status == 'Лид'))
            experience = [row[0] for row in result]
            return experience


async def leads_education(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.education).where(User.status == 'Лид'))
            education = [row[0] for row in result]
            return education


async def leads_id(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User.user_id).where(User.status == 'Лид'))
            user_id = [row[0] for row in result]
            return user_id


async def number_registered(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(func.count(User.user_id))
            users = result.scalar()
            return users


async def number_remote(session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(func.count()).where(User.status == 'Удален'))
            remote = result.scalar()
            return remote
