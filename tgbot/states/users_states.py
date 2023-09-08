from aiogram.fsm.state import State, StatesGroup


class Questionnaire(StatesGroup):
    name = State()
    city = State()
    vacancies = State()
    employment = State()
    schedule = State()


class CityRequest(StatesGroup):
    city = State()


class Data(StatesGroup):
    schedule = State()
    full_name = State()
    age = State()


class Questions(StatesGroup):
    question = State()
