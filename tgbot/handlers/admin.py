from aiogram.filters import Command, and_f, or_f
from aiogram.types import CallbackQuery
from aiogram import Router, F, types
from environs import Env
from sqlalchemy.orm import sessionmaker

from lexiocon.admin_lexicon import ADMIN
from filters.admin_filters import IsAdmin
from keyboards.admin_keyboards import admin_menu_kb, category_kb, \
                                      manipuations_kb_2, \
                                      function, MyCallbackFactory
from database.users import update_status
from database.admin import number_applicants, applicants_name, \
                           applicants_city, applicants_vacancies, \
                           applicants_employment, applicants_schedule, \
                           applicants_user_name, applicants_id, \
                           number_satisfied, satisfied_name, \
                           satisfied_city, satisfied_vacancies, \
                           satisfied_employment, satisfied_schedule, \
                           satisfied_user_name, satisfied_id

admin_router: Router = Router()

env = Env()
env.read_env()


@admin_router.callback_query(F.data == 'back_menu_admin_pressed')
@admin_router.message(and_f(Command(commands=['admin'])),
                      IsAdmin(env('ADMIN_IDS')))
async def open_admin(update: types.update):
    if isinstance(update, types.CallbackQuery):
        await update.message.edit_text(text=ADMIN['greetings'],
                                       reply_markup=admin_menu_kb)
    elif isinstance(update, types.Message):
        await update.answer(text=ADMIN['greetings'],
                            reply_markup=admin_menu_kb)


@admin_router.callback_query(F.data == 'statistics')
async def open_statistics(callback: CallbackQuery,
                          session_maker: sessionmaker):
    await callback.message.edit_text(text='Разработка данного раздела завершена на 70%')


@admin_router.callback_query(F.data == 'applications_pressed')
async def choose_category(callback: CallbackQuery):
    await callback.message.edit_text(text=ADMIN['select_category'],
                                     reply_markup=category_kb)


@admin_router.callback_query(or_f(F.data == 'looking_for_work_pressed',
                                  F.data == 'update_pressed'))
async def show_applicants(callback: CallbackQuery,
                          session_maker: sessionmaker):
    await callback.message.edit_text(text=ADMIN['time'])
    applicants = await number_applicants(session_maker=session_maker)
    names = await applicants_name(session_maker=session_maker)
    city = await applicants_city(session_maker=session_maker)
    vacancies = await applicants_vacancies(session_maker=session_maker)
    employment = await applicants_employment(session_maker=session_maker)
    schedule = await applicants_schedule(session_maker=session_maker)
    user_name = await applicants_user_name(session_maker=session_maker)
    user_id = await applicants_id(session_maker=session_maker)
    for i in range(int(applicants)):
        await callback.message.answer(text=f'Имя: {names[i]}\n'
                                      f'Город: {city[i]}\nВакансия: '
                                      f'{vacancies[i]}\nВид трудусьтройства: '
                                      f'{employment[i]}\nРасписание: '
                                      f'{schedule[i]}\n'
                                      f'https://t.me/{user_name[i]}',
                                      reply_markup=function(user_id[i]))
    await callback.message.answer(text='Список пользователей окончен',
                                  reply_markup=manipuations_kb_2)


@admin_router.callback_query(MyCallbackFactory.filter(F.subcategory == 1))
async def move_dissatisfied(callback: CallbackQuery,
                            session_maker: sessionmaker):
    await update_status(int(callback.data[4:-2]), 'Не устраивает',
                        session_maker=session_maker)
    await callback.message.edit_text(text=ADMIN['move_dissatisfied'])


@admin_router.callback_query(MyCallbackFactory.filter(F.subcategory == 2))
async def move_suits(callback: CallbackQuery,
                     session_maker: sessionmaker):
    await update_status(int(callback.data[4:-2]), 'Устраивает',
                        session_maker=session_maker)
    await callback.message.edit_text(text=ADMIN['move_suits'])


@admin_router.callback_query(or_f(F.data == 'satisfied_offer_pressed',
                                  F.data == 'update_pressed1'))
async def show_satisfied(callback: CallbackQuery,
                         session_maker: sessionmaker):
    await callback.message.edit_text(text=ADMIN['time'])
    satisfied = await number_satisfied(session_maker=session_maker)
    names = await satisfied_name(session_maker=session_maker)
    city = await satisfied_city(session_maker=session_maker)
    vacancies = await satisfied_vacancies(session_maker=session_maker)
    employment = await satisfied_employment(session_maker=session_maker)
    schedule = await satisfied_schedule(session_maker=session_maker)
    user_name = await satisfied_user_name(session_maker=session_maker)
    user_id = await satisfied_id(session_maker=session_maker)
    for i in range(int(satisfied)):
        await callback.message.answer(text=f'Имя: {names[i]}\n'
                                      f'Город: {city[i]}\nВакансия: '
                                      f'{vacancies[i]}\nВид трудусьтройства: '
                                      f'{employment[i]}\nРасписание: '
                                      f'{schedule[i]}\n'
                                      f'https://t.me/{user_name[i]}')
    await callback.message.answer(text='Список пользователей окончен',
                                  reply_markup=manipuations_kb_2)
