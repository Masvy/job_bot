from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from lexiocon.user_lexicon import USERS
from states.users_states import Questionnaire
from keyboards.user_keyboards import back_menu_kb, consent_questionnaire_kb, \
                                     yes_or_no_kb

employment_router: Router = Router()


@employment_router.callback_query(F.data == 'employment_pressed')
async def employ(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['employment_info'],
                                     reply_markup=consent_questionnaire_kb)


@employment_router.callback_query(F.data == 'agreement_pressed')
async def warn_user(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['agreement'],
                                     reply_markup=yes_or_no_kb)


@employment_router.callback_query(F.data == 'yes_pressed', StateFilter(default_state))
async def request_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=USERS['name_request'])
    await state.set_state(Questionnaire.name)


@employment_router.message(StateFilter(Questionnaire.name))
async def request_city(message: Message, state: FSMContext):
    await message.answer(text=USERS['city_request'])
    await state.set_state(Questionnaire.city)


@employment_router.message(StateFilter(Questionnaire.city))
async def request_vacancies(message: Message, state: FSMContext):
    await message.answer(text=USERS['vacancies_request'])
    await state.set_state(Questionnaire.vacancies)


@employment_router.message(StateFilter(Questionnaire.vacancies))
async def request_employment(message: Message, state: FSMContext):
    await message.answer(text=USERS['type_employment'])
    await state.set_state(Questionnaire.employment)


@employment_router.message(StateFilter(Questionnaire.employment))
async def request_schedule(message: Message, state: FSMContext):
    await message.answer(text=USERS['schedule'])
    await state.set_state(Questionnaire.schedule)


@employment_router.message(StateFilter(Questionnaire.schedule))
async def complete_questionnaire(message: Message, state: FSMContext):
    await message.answer(text=USERS['end_questionnaire'],
                         reply_markup=back_menu_kb)
    await state.clear()


@employment_router.callback_query(F.data == 'refusal_pressed')
async def thank_contacting(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['refusal'],
                                     reply_markup=back_menu_kb)
