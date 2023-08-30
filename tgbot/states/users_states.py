from aiogram.fsm.state import State, StatesGroup


class Questionnaire(StatesGroup):
    name = State()
    city = State()
    vacancies = State()
    employment = State()
    schedule = State()
