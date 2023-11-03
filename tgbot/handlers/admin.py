from aiogram.filters import Command, and_f, or_f
from aiogram.types import CallbackQuery
from aiogram import Router, F, types
from environs import Env
from sqlalchemy.orm import sessionmaker

from lexiocon.admin_lexicon import ADMIN
from filters.admin_filters import IsAdmin
from keyboards.admin_keyboards import admin_menu_kb, category_kb, \
    manipuations_kb_1, \
    function, function2, \
    MyCallbackFactory, manipuations_kb_2, \
    manipuations_kb_3
from database.users import update_status
from database.admin import number_applicants, applicants_name, \
    applicants_city, applicants_vacancies, \
    applicants_employment, applicants_schedule, \
    applicants_id, \
    applicants_age, applicants_experience, \
    applicants_education, applicants_question, \
    number_satisfied, satisfied_name, \
    satisfied_city, satisfied_vacancies, \
    satisfied_employment, satisfied_schedule, \
    satisfied_id, \
    satisfied_age, satisfied_experience, \
    satisfied_education, \
    number_leads, leads_name, leads_city, \
    leads_vacancies, leads_employment, \
    leads_schedule, \
    leads_age, leads_experience, leads_education, \
    number_registered, leads_user_name, satisfied_user_name, \
    applicants_user_name

admin_router: Router = Router()

env = Env()
env.read_env()


@admin_router.callback_query(F.data == 'back_menu_admin_pressed')
@admin_router.message(and_f(Command(commands=['admin'])),
                      IsAdmin(env('ADMIN_IDS')))
async def open_admin(update: types.update):
    '''Этот хендлер реагирует на команду /admin'''
    if isinstance(update, types.CallbackQuery):
        await update.message.edit_text(text=ADMIN['greetings'],
                                       reply_markup=admin_menu_kb)
    elif isinstance(update, types.Message):
        await update.answer(text=ADMIN['greetings'],
                            reply_markup=admin_menu_kb)


@admin_router.callback_query(F.data == 'statistics_pressed')
async def open_statistics(callback: CallbackQuery,
                          session_maker: sessionmaker):
    '''Этот хендлер реагирует на кнопку Статистика'''
    users = await number_registered(session_maker=session_maker)
    applicants = await number_applicants(session_maker=session_maker)
    satisfied = await number_satisfied(session_maker=session_maker)
    leads = await number_leads(session_maker=session_maker)
    await callback.message.edit_text(text='Количество пользователей: '
                                     f'{users}\nКоличество соискателей: '
                                     f'{applicants}\nКоличество тех, кого '
                                     f'устроило предложение: {satisfied}\n'
                                     f'Количество лидов: {leads}',
                                     reply_markup=manipuations_kb_3)


@admin_router.callback_query(F.data == 'applications_pressed')
async def choose_category(callback: CallbackQuery):
    '''Этот хендлер реагирует на кнопку Просмотреть заявки'''
    await callback.message.edit_text(text=ADMIN['select_category'],
                                     reply_markup=category_kb)


@admin_router.callback_query(or_f(F.data == 'looking_for_work_pressed',
                                  F.data == 'update_pressed'))
async def show_applicants(callback: CallbackQuery,
                          session_maker: sessionmaker):
    '''Этот хендлер реагирует на кнопку В поисках работы'''
    await callback.message.edit_text(text=ADMIN['time'])
    applicants = await number_applicants(session_maker=session_maker)
    names = await applicants_name(session_maker=session_maker)
    user_name = await applicants_user_name(session_maker=session_maker)
    city = await applicants_city(session_maker=session_maker)
    vacancies = await applicants_vacancies(session_maker=session_maker)
    employment = await applicants_employment(session_maker=session_maker)
    schedule = await applicants_schedule(session_maker=session_maker)
    user_id = await applicants_id(session_maker=session_maker)
    age = await applicants_age(session_maker=session_maker)
    experience = await applicants_experience(session_maker=session_maker)
    education = await applicants_education(session_maker=session_maker)
    question = await applicants_question(session_maker=session_maker)
    for i in range(int(applicants)):
        await callback.message.answer(text=f'Имя: {names[i]}\n'
                                      f'Возраст: {age[i]}\n'
                                      f'Город: {city[i]}\nВакансия: '
                                      f'{vacancies[i]}\nВид трудоустройства: '
                                      f'{employment[i]}\nРасписание: '
                                      f'{schedule[i]}\n'
                                      f'Опыт работы: {experience[i]}\n'
                                      f'Образование: {education[i]}\n'
                                      f'Вопрос: {question[i]}\n'
                                      f'Ссылка на пользователя: @{user_name[i]}',
                                      reply_markup=function(user_id[i]))
    await callback.message.answer(text='Список пользователей окончен',
                                  reply_markup=manipuations_kb_1)


@admin_router.callback_query(MyCallbackFactory.filter(F.subcategory == 1))
async def move_dissatisfied(callback: CallbackQuery,
                            session_maker: sessionmaker):
    '''Этот хендлер реагирует на генерируемую callback_data'''
    await update_status(int(callback.data[4:-2]), 'Не устраивает',
                        session_maker=session_maker)
    await callback.message.edit_text(text=ADMIN['move_dissatisfied'])


@admin_router.callback_query(MyCallbackFactory.filter(F.subcategory == 2))
async def move_suits(callback: CallbackQuery,
                     session_maker: sessionmaker):
    'Этот хендлер реагирует на генерируемую callback_data'
    await update_status(int(callback.data[4:-2]), 'Устраивает',
                        session_maker=session_maker)
    await callback.message.edit_text(text=ADMIN['move_suits'])


@admin_router.callback_query(or_f(F.data == 'satisfied_offer_pressed',
                                  F.data == 'update_pressed_2'))
async def show_satisfied(callback: CallbackQuery,
                         session_maker: sessionmaker):
    'Этот хендлер реагирует на кнопку Устраивает предложение'
    await callback.message.edit_text(text=ADMIN['time'])
    satisfied = await number_satisfied(session_maker=session_maker)
    names = await satisfied_name(session_maker=session_maker)
    user_name = await satisfied_user_name(session_maker=session_maker)
    city = await satisfied_city(session_maker=session_maker)
    vacancies = await satisfied_vacancies(session_maker=session_maker)
    employment = await satisfied_employment(session_maker=session_maker)
    schedule = await satisfied_schedule(session_maker=session_maker)
    user_id = await satisfied_id(session_maker=session_maker)
    age = await satisfied_age(session_maker=session_maker)
    experience = await satisfied_experience(session_maker=session_maker)
    education = await satisfied_education(session_maker=session_maker)
    for i in range(int(satisfied)):
        await callback.message.answer(text=f'Имя: {names[i]}\n'
                                      f'Возраст: {age[i]}\n'
                                      f'Город: {city[i]}\nВакансия: '
                                      f'{vacancies[i]}\nВид трудоустройства: '
                                      f'{employment[i]}\nРасписание: '
                                      f'{schedule[i]}\n'
                                      f'Опыт работы: {experience[i]}\n'
                                      f'Образование: {education[i]}\n'
                                      f'Ссылка на пользователя: @{user_name[i]}',
                                      reply_markup=function2(user_id[i]))
    await callback.message.answer(text='Список пользователей окончен',
                                  reply_markup=manipuations_kb_2)


@admin_router.callback_query(MyCallbackFactory.filter(F.subcategory == 3))
async def add_lead(callback: CallbackQuery,
                   session_maker: sessionmaker):
    'Этот хендлер реагирует на генерируемую callback_data'
    await update_status(int(callback.data[4:-2]), 'Лид',
                        session_maker=session_maker)
    await callback.message.edit_text(text=ADMIN['move_leads'])


@admin_router.callback_query(F.data == 'list_leads_pressed')
async def show_leads(callback: CallbackQuery,
                     session_maker: sessionmaker):
    'Этот хендлер реагирует на кнопку Список лидов'
    await callback.message.edit_text(text=ADMIN['time'])
    leads = await number_leads(session_maker=session_maker)
    names = await leads_name(session_maker=session_maker)
    user_name = await leads_user_name(session_maker=session_maker)
    city = await leads_city(session_maker=session_maker)
    vacancies = await leads_vacancies(session_maker=session_maker)
    employment = await leads_employment(session_maker=session_maker)
    schedule = await leads_schedule(session_maker=session_maker)
    age = await leads_age(session_maker=session_maker)
    experience = await leads_experience(session_maker=session_maker)
    education = await leads_education(session_maker=session_maker)
    for i in range(int(leads)):
        await callback.message.answer(text=f'Имя: {names[i]}\n'
                                      f'Возраст: {age[i]}\n'
                                      f'Город: {city[i]}\nВакансия: '
                                      f'{vacancies[i]}\nВид трудоустройства: '
                                      f'{employment[i]}\nРасписание: '
                                      f'{schedule[i]}\n'
                                      f'Опыт работы: {experience[i]}\n'
                                      f'Образование: {education[i]}\n'
                                      f'Ссылка на пользователя: @{user_name[i]}')
    await callback.message.answer(text='Список пользователей окончен',
                                  reply_markup=manipuations_kb_3)
