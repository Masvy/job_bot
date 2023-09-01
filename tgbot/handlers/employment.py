from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import StateFilter, or_f
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm import sessionmaker

from lexiocon.user_lexicon import USERS
from states.users_states import Questionnaire
from keyboards.user_keyboards import back_menu_kb, consent_questionnaire_kb, \
                                     yes_or_no_kb, true_false_kb
from database.users import update_name, update_city, update_vacancies, \
                           update_employment, update_schedule, \
                           update_status, read_data

employment_router: Router = Router()


@employment_router.callback_query(F.data == 'employment_pressed')
async def employ(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['employment_info'],
                                     reply_markup=consent_questionnaire_kb)


@employment_router.callback_query(F.data == 'agreement_pressed')
async def warn_user(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['agreement'],
                                     reply_markup=yes_or_no_kb)


@employment_router.callback_query(or_f(F.data == 'yes_pressed',
                                       F.data == 'correct_pressed'),
                                       StateFilter(default_state))
async def request_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=USERS['name_request'])
    await state.set_state(Questionnaire.name)


@employment_router.message(StateFilter(Questionnaire.name))
async def request_city(message: Message, state: FSMContext,
                       session_maker: sessionmaker):
    await update_name(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text=USERS['city_request'])
    await state.set_state(Questionnaire.city)


@employment_router.message(StateFilter(Questionnaire.city))
async def request_vacancies(message: Message, state: FSMContext,
                            session_maker: sessionmaker):
    await update_city(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text=USERS['vacancies_request'])
    await state.set_state(Questionnaire.vacancies)


@employment_router.message(StateFilter(Questionnaire.vacancies))
async def request_employment(message: Message, state: FSMContext,
                             session_maker: sessionmaker):
    await update_vacancies(message.from_user.id, message.text,
                           session_maker=session_maker)
    await message.answer(text=USERS['type_employment'])
    await state.set_state(Questionnaire.employment)


@employment_router.message(StateFilter(Questionnaire.employment))
async def request_schedule(message: Message, state: FSMContext,
                           session_maker: sessionmaker):
    await update_employment(message.from_user.id, message.text,
                            session_maker=session_maker)
    await message.answer(text=USERS['schedule'])
    await state.set_state(Questionnaire.schedule)


@employment_router.message(StateFilter(Questionnaire.schedule))
async def check_result(message: Message, state: FSMContext,
                       session_maker: sessionmaker):
    await update_schedule(message.from_user.id, message.text,
                          session_maker=session_maker)
    data = await read_data(message.from_user.id, session_maker=session_maker)
    await message.answer(text='Проверьте, пожалуйста, всё ли верно?\n'
                         f'Имя: {data["name"]}\nГород: '
                         f'{data["city"]}\nВакансия: '
                         f'{data["vacancies"]}\nВид трудоустройства: '
                         f'{data["employment"]}\nРасписание: '
                         f'{data["schedule"]}',
                         reply_markup=true_false_kb)
    await state.clear()


@employment_router.callback_query(F.data == 'all_right_pressed')
async def complete_questionnaire(callback: CallbackQuery,
                                 session_maker: sessionmaker):
    await update_status(callback.from_user.id, 'Устраивает',
                        session_maker=session_maker)
    await callback.message.edit_text(USERS['end_questionnaire'],
                                     reply_markup=back_menu_kb)


@employment_router.callback_query(F.data == 'refusal_pressed')
async def thank_contacting(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['refusal'],
                                     reply_markup=back_menu_kb)
