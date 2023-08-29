from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker
from aiogram.filters import CommandStart

from lexiocon.user_lexicon import USERS
from database.users import read_status, update_status
from keyboards.user_keyboards import main_menu_kb, back_menu_kb, yes_or_no_kb

start_router: Router = Router()


@start_router.callback_query(F.data == 'back_menu_pressed')
@start_router.message(CommandStart())
async def start_bot(update: types.update):
    if isinstance(update, types.CallbackQuery):
        await update.message.edit_text(text=USERS['main_manu'],
                                       reply_markup=main_menu_kb)
    elif isinstance(update, types.Message):
        await update.answer(text=USERS['greetings'],
                            reply_markup=main_menu_kb)


@start_router.callback_query(F.data == 'vacancies_pressed')
async def show_vacancies(callback: CallbackQuery,
                         session_maker: sessionmaker):
    status = await read_status(callback.from_user.id,
                               session_maker=session_maker)
    if status == 0:
        await callback.message.edit_text(text=USERS['no_access'],
                                         reply_markup=back_menu_kb)
    else:
        await callback.message.edit_text(text='Вакансий на данный момент нет')


@start_router.callback_query(F.data == 'company_pressed')
async def show_company(callback: CallbackQuery,
                       session_maker: sessionmaker):
    await callback.message.edit_text(text=USERS['company'],
                                     reply_markup=back_menu_kb)
    status = await read_status(callback.from_user.id,
                               session_maker=session_maker)
    if status == 0:
        await update_status(callback.from_user.id,
                            session_maker=session_maker)
    else:
        pass


@start_router.callback_query(F.data == 'employment_pressed')
async def employ(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['employment_info'],
                                     reply_markup=yes_or_no_kb)


@start_router.callback_query(F.data == 'yes_pressed')
async def warn_user(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['agreement'])


@start_router.callback_query(F.data == 'no_pressed')
async def thank_contacting(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['refusal'],
                                     reply_markup=back_menu_kb)