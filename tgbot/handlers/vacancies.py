from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker

from lexiocon.user_lexicon import USERS
from database.users import read_status
from keyboards.user_keyboards import back_menu_kb

vacanties_router: Router = Router()


@vacanties_router.callback_query(F.data == 'vacancies_pressed')
async def show_vacancies(callback: CallbackQuery,
                         session_maker: sessionmaker):
    status = await read_status(callback.from_user.id,
                               session_maker=session_maker)
    if status == 0:
        await callback.message.edit_text(text=USERS['no_access'],
                                         reply_markup=back_menu_kb)
    else:
        await callback.message.edit_text(text='Вакансий на данный момент нет',
                                         reply_markup=back_menu_kb)
