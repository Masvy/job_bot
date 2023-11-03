from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker
from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


from lexiocon.user_lexicon import USERS, VACANCIES
from states.users_states import Questionnaire, CityRequest, Data, Questions
from database.users import update_access
from keyboards.user_keyboards import vacancies_kb, company_kb, \
                                     employments_kb_1, experience_kb, \
                                     education_kb, back_menu_kb, \
                                     questions_kb, employments_kb_2, manager_kb
from database.users import update_city, update_vacancies, update_employment, \
                           update_schedule, update_name, update_age, \
                           update_experience, update_education, \
                           update_status, update_question

vacanties_router: Router = Router()


@vacanties_router.callback_query(F.data == 'vacancies_pressed')
async def show_vacancies(callback: CallbackQuery,
                         session_maker: sessionmaker):
    await update_access(callback.from_user.id, 2, session_maker=session_maker)
    await callback.message.answer(text=USERS['interesting_vacancies'],
                                  reply_markup=vacancies_kb)


@vacanties_router.callback_query(or_f(F.data == 'Водитель',
                                       F.data == 'Менеджер по продажам',
                                       F.data == 'Продавец-кассир',
                                       F.data == 'Разнорабочий',
                                       F.data == 'Администратор',
                                       F.data == 'back_vacancies_pressed'))
async def show_description_3(callback: CallbackQuery,
                             session_maker: sessionmaker):
    '''Этот хендлер реагирует на кнопки Водитель/Менеджер по продажам'''
    await update_vacancies(callback.from_user.id, callback.data,
                           session_maker=session_maker)
    if callback.data == 'Водитель':
        await callback.message.edit_text(text=VACANCIES['driver'])
        await callback.message.answer(text=USERS['types_employment_1'],
                                      reply_markup=employments_kb_1)
    elif callback.data == 'Менеджер по продажам':
        await callback.message.edit_text(text=VACANCIES['sales_manager'])
        await callback.message.answer(text=USERS['types_employment_2'],
                                      reply_markup=employments_kb_2)
    elif callback.data == 'Продавец-кассир':
        await callback.message.edit_text(text=VACANCIES['salesman-cashier'])
        await callback.message.answer(text=USERS['types_employment_3'],
                                      reply_markup=employments_kb_2)

    elif callback.data == 'Разнорабочий':
        await callback.message.edit_text(text=VACANCIES['handyman'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_kb_2)

    elif callback.data == 'Администратор':
        await callback.message.edit_text(text=VACANCIES['administrator'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_kb_2)
    
        

@vacanties_router.message(StateFilter(Questionnaire.city))
async def request_city_2(callback: CallbackQuery,
                         state: FSMContext):
    await callback.message.edit_text(text=USERS['city_input_2'])
    await state.set_state(CityRequest.city)