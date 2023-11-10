from aiogram.fsm.state import State, StatesGroup


class Company(StatesGroup):
    city = State()
    vacancies = State()
    employment = State()
    schedule = State()
    name = State()
    age = State()
    experience = State()
    education = State()


class Vacancies(StatesGroup):
    vacancies = State()
    employment = State()
    schedule = State()
    experience = State()
    education = State()
    city = State()
    name = State()
    age = State()


class Employments(StatesGroup):
    city = State()
    vacancies = State()
    employment = State()
    schedule = State()
    name = State()
    age = State()
    experience = State()
    education = State()


class QuestionsCompany(StatesGroup):
    question = State()


class QuestionsVacancies(StatesGroup):
    question = State()


class QuestionsEmployments(StatesGroup):
    question = State()
