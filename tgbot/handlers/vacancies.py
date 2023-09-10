from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker

from database.users import update_access
from keyboards.user_keyboards import back_menu_kb

vacanties_router: Router = Router()


@vacanties_router.callback_query(F.data == 'vacancies_pressed')
async def show_vacancies(callback: CallbackQuery,
                         session_maker: sessionmaker):
    await update_access(callback.from_user.id, 2, session_maker=session_maker)
    await callback.message.edit_text(text='Вакансий на данный момент нет',
                                     reply_markup=back_menu_kb)
