from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker
from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexiocon.user_lexicon import USERS, VACANCIES
from states.users_states import CityRequest, Data, Questions
from keyboards.user_keyboards import company_kb, vacancies_kb, \
                                     employments_kb_1, experience_kb, \
                                     education_kb, back_menu_kb, \
                                     questions_kb, employments_kb_2
from database.users import update_access, update_city, \
                           update_vacancies, update_employment, \
                           update_schedule, update_name, update_age, \
                           update_experience, update_education, \
                           update_status, update_question

company_router: Router = Router()


@company_router.callback_query(F.data == 'company_pressed')
async def show_company(callback: CallbackQuery):
    '''Этот хендлер реагирует на кнопку О компании'''
    await callback.message.edit_text(text=USERS['company'])
    await callback.message.answer(text=USERS['jobs_in_city'],
                                  reply_markup=company_kb)


@company_router.callback_query(F.data == 'show_vacancies_pressed',
                               StateFilter(default_state))
async def request_city(callback: CallbackQuery,
                       state: FSMContext):
    '''Этот хендлер реагирует на кнопку Просмотреть вакансии'''
    await callback.message.edit_text(text=USERS['city_input_2'])
    await state.set_state(CityRequest.city)


@company_router.message(StateFilter(CityRequest.city))
async def show_vacancies(message: Message,
                         state: FSMContext,
                         session_maker: sessionmaker):
    await update_city(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text=USERS['interesting_vacancies'],
                         reply_markup=vacancies_kb)
    await state.clear()


@company_router.callback_query(or_f(F.data == 'Водитель',
                                    F.data == 'Менеджер по продажам'))
async def show_description(callback: CallbackQuery,
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


@company_router.callback_query(or_f(F.data == 'Полная занятость',
                                    F.data == 'Частичная занятость',
                                    F.data == 'Подработка'),
                                    StateFilter(default_state))
async def request_employment(callback: CallbackQuery,
                             session_maker: sessionmaker,
                             state: FSMContext):
    '''
    Этот хендлер реагирует на кнопки Полная занятость/Частичная занятость/Подработка


    '''
    await update_employment(callback.from_user.id, callback.data,
                            session_maker=session_maker)
    if callback.data == 'Полная занятость':
        await callback.message.edit_text(text='Какой график работы вас '
                                         'интересует?')
    elif callback.data == 'Частичная занятость':
        await callback.message.edit_text(text='Сколько часов в день вы '
                                         'готовы уделять работе?')
    else:
        await callback.message.edit_text(text='Сколько часов в день вы '
                                         'готовы уделять работе?')
    await state.set_state(Data.schedule)


@company_router.message(StateFilter(Data.schedule))
async def request_full_name(message: Message, state: FSMContext,
                            session_maker: sessionmaker):

    await update_schedule(message.from_user.id, message.text,
                          session_maker=session_maker)
    await message.answer(text='Отлично! Чтобы ускорить процесс '
                              'трудоустройства, вы можете заполнить '
                              'анкету сейчас. Укажите полностью ваше '
                              'ФИО:')
    await state.set_state(Data.full_name)


@company_router.message(StateFilter(Data.full_name),
                        lambda x: 2 <= len(x.text.split()) <= 3)
async def request_age(message: Message, state: FSMContext,
                      session_maker: sessionmaker):
    await update_name(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text='Приятно познакомиться, '
                         f'{message.text.split()[1]}.\nУкажите '
                         'ваш возраст:')
    await state.set_state(Data.age)


@company_router.message(StateFilter(Data.full_name))
async def incorrect_name(message: Message):
    await message.answer(text='Это не очень похоже на ФИО')


@company_router.message(StateFilter(Data.age),
                        lambda x: x.text.isdigit())
async def request_expirience(message: Message, state: FSMContext,
                             session_maker: sessionmaker):
    await update_age(message.from_user.id, int(message.text),
                     session_maker=session_maker)
    await message.answer(text='У вас есть опыт работы в данной подобной '
                         'должности?', reply_markup=experience_kb)
    await state.clear()


@company_router.message(StateFilter(Data.age))
async def incorrect_age(message: Message):
    await message.answer(text='Это не очень похоже на возраст')


@company_router.callback_query(or_f(F.data == 'Да',
                                    F.data == 'Нет'))
async def requst_education(callback: CallbackQuery,
                           session_maker: sessionmaker):
    await update_experience(callback.from_user.id, callback.data,
                            session_maker=session_maker)
    await callback.message.edit_text(text='Укажите уровень вашего '
                                     'образования:',
                                     reply_markup=education_kb)


@company_router.callback_query(or_f(F.data == 'Общее',
                                    F.data == 'Среднее',
                                    F.data == 'Высшее'))
async def requst_question(callback: CallbackQuery,
                          session_maker: sessionmaker):
    await update_education(callback.from_user.id, callback.data,
                           session_maker=session_maker)
    await update_access(callback.from_user.id, 1, session_maker=session_maker)
    await callback.message.edit_text(text='Первичная анкета заполнена и '
                                     'передана специалисту. В течении 3 '
                                     'рабочих дней с вами свяжества менеджер '
                                     'и назначит дату встречи для '
                                     'обсуждения деталей работы.\n')
    await callback.message.answer(text='На собеседование возьмите с собой '
                                  'следующие документы:\n\t📌 Паспорт'
                                  ';\n\t📌 ИНН;\n\t📌 Документ, подтверждающий '
                                  'образование.\nПосле собеседования '
                                  'менеджер предложит вам сразу заключить '
                                  'трудовой договор/ГПХ и приступить к работе '
                                  'на следующий день.')
    await callback.message.answer(text='Зарплатный проект нашей компании '
                                  'предоставляет банк "название".\nБанк 🏦 '
                                  '"Название" является нашим партнером и при '
                                  'трудоустройстве в договоренеобходимо '
                                  'указать номер счета, привязанный к '
                                  'зарплатному проекту.\nВсе расходы по '
                                  'обслуживанию зарплатной карты несет наша '
                                  'компания, поэтому для вас карта будет '
                                  'совершенно бесплатна.\nЧтобы привязать '
                                  '💳 карту к нашему зарплатному проекту, '
                                  'закажите ее по ссылке: ссылка')
    await callback.message.answer(text='Чтобы получать выплаты заработной '
                                  'платы с первого рабочего дня, закажите '
                                  'карту прямо сейчас, т.к. ее изготовление '
                                  'занимает несколько дней, а при заключении '
                                  'трудового договора, она вам потребуется.'
                                  '\n\nУ вас остались какие-то вопросы?',
                                  reply_markup=questions_kb)


@company_router.callback_query(F.data == 'no_questions_pressed')
async def respond_rejection(callabck: CallbackQuery,
                            session_maker: sessionmaker):
    await update_status(callabck.from_user.id, 'Соискатель',
                        session_maker=session_maker)
    await callabck.message.edit_text(text='Отлично! В течении 3-х рабочих '
                                     'дней с вами свяжется менеджер и '
                                     'назначит дату собеседования',
                                     reply_markup=back_menu_kb)


@company_router.callback_query(F.data == 'questions_pressed',
                               StateFilter(default_state))
async def respond_consent(callback: CallbackQuery,
                          state: FSMContext):
    await callback.message.edit_text(text='Хорошо, можете задать ваш вопрос:')
    await state.set_state(Questions.question)


@company_router.message(StateFilter(Questions.question))
async def answer_question(message: Message, state: FSMContext,
                          session_maker: sessionmaker):
    await update_question(message.from_user.id, message.text,
                          session_maker=session_maker)
    await update_status(message.from_user.id, 'Соискатель',
                        session_maker=session_maker)
    await message.answer(text='Я передам ваш вопрос менеджеру, он свяжется с '
                         'вами в течении 3-х рабочих дней и даст ответ на '
                         'этот и другие вопросы.',
                         reply_markup=back_menu_kb)
    await state.clear()
