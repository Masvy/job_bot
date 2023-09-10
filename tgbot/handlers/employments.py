from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker
from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexiocon.user_lexicon import USERS
from states.users_states import CityRequest, Data, Questions
from keyboards.user_keyboards import company_kb, vacancies_kb, \
                                     employments_kb, experience_kb, \
                                     education_kb, back_menu_kb, \
                                     questions_kb
from database.users import update_city, update_vacancies, update_employment, \
                           update_schedule, update_name, update_age, \
                           update_experience, update_education, \
                           update_status, update_question

employment_router: Router = Router()


@employment_router.callback_query(F.data == 'employment_pressed')
async def employ(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['jobs_in_city'],
                                     reply_markup=company_kb)


@employment_router.callback_query(F.data == 'show_vacancies_pressed',
                                  StateFilter(default_state))
async def request_city_2(callback: CallbackQuery,
                         state: FSMContext):
    await callback.message.edit_text(text=USERS['city_input_2'])
    await state.set_state(CityRequest.city)


@employment_router.message(StateFilter(CityRequest.city))
async def show_vacancies_2(message: Message,
                           state: FSMContext,
                           session_maker: sessionmaker):
    await update_city(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text=USERS['interesting_vacancies'],
                         reply_markup=vacancies_kb)
    await state.clear()


@employment_router.callback_query(F.data == 'Водитель')
async def show_description_2(callback: CallbackQuery,
                             session_maker: sessionmaker):
    await update_vacancies(callback.from_user.id, callback.data,
                           session_maker=session_maker)
    await callback.message.edit_text(text='Вакансия 1: Водитель\nЗП от '
                                     '65 000 рублей с ежедневными выплатами '
                                     'на карту.\n\nОбязанности:\nОбеспечение '
                                     'своевременной доставки грузов.\n\n'
                                     'Требования:\nВодительское удостоверение '
                                     'категории В/С;\nСтаж от 1 года\n\n'
                                     'Условия труда:\nСлужебный автомобиль '
                                     '“Марка”;')
    await callback.message.answer(text=USERS['types_employment'])
    await callback.message.answer(text='Полная занятость - Полный рабочий '
                                  'день (2/2, 3/3, 5/2):',
                                  reply_markup=employments_kb)


@employment_router.callback_query(F.data == 'Полная занятость',
                                  StateFilter(default_state))
async def request_employment_2(callback: CallbackQuery, state: FSMContext,
                               session_maker: sessionmaker):
    await update_employment(callback.from_user.id, callback.data,
                            session_maker=session_maker)
    await callback.message.edit_text(text='Какой график работы вас '
                                     'интересует?')
    await state.set_state(Data.schedule)


@employment_router.message(StateFilter(Data.schedule))
async def request_full_name_2(message: Message, state: FSMContext,
                              session_maker: sessionmaker):
    await update_schedule(message.from_user.id, message.text,
                          session_maker=session_maker)
    await message.answer(text='Отлично! Чтобы ускорить процесс '
                         'трудоустройства, вы можете заполнить '
                         'анкету сейчас. Укажите полностью ваше '
                         'ФИО:')
    await state.set_state(Data.full_name)


@employment_router.message(StateFilter(Data.full_name))
async def request_age_2(message: Message, state: FSMContext,
                        session_maker: sessionmaker):
    await update_name(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text='Приятно познакомиться, '
                         f'{message.text.split()[1]}.\nУкажите '
                         'ваш возраст:')
    await state.set_state(Data.age)


@employment_router.message(StateFilter(Data.age))
async def request_expirience_2(message: Message, state: FSMContext,
                               session_maker: sessionmaker):
    await update_age(message.from_user.id, int(message.text),
                     session_maker=session_maker)
    await message.answer(text='У вас есть опыт работы в данной подобной '
                         'должности?', reply_markup=experience_kb)
    await state.clear()


@employment_router.callback_query(or_f(F.data == 'Да',
                                       F.data == 'Нет'))
async def requst_education_2(callback: CallbackQuery,
                             session_maker: sessionmaker):
    await update_experience(callback.from_user.id, callback.data,
                            session_maker=session_maker)
    await callback.message.edit_text(text='Укажите уровень вашего '
                                     'образования:',
                                     reply_markup=education_kb)


@employment_router.callback_query(or_f(F.data == 'Общее',
                                       F.data == 'Среднее',
                                       F.data == 'Высшее'))
async def requst_question_2(callback: CallbackQuery,
                            session_maker: sessionmaker):
    await update_education(callback.from_user.id, callback.data,
                           session_maker=session_maker)
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


@employment_router.callback_query(F.data == 'no_questions_pressed')
async def respond_rejection_2(callabck: CallbackQuery,
                              session_maker: sessionmaker):
    await update_status(callabck.from_user.id, 'Соискатель',
                        session_maker=session_maker)
    await callabck.message.edit_text(text='Отлично! В течении 3-х рабочих '
                                     'дней с вами свяжется менеджер и '
                                     'назначит дату собеседования',
                                     reply_markup=back_menu_kb)


@employment_router.callback_query(F.data == 'questions_pressed',
                                  StateFilter(default_state))
async def respond_consent_2(callback: CallbackQuery,
                            state: FSMContext):
    await callback.message.edit_text(text='Хорошо, можете задать ваш вопрос:')
    await state.set_state(Questions.question)


@employment_router.message(StateFilter(Questions.question))
async def answer_question_2(message: Message, state: FSMContext,
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
