from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker
from aiogram.filters import CommandStart

from lexiocon.user_lexicon import USERS
from database.users import read_access, update_access
from keyboards.user_keyboards import main_menu_kb, back_menu_kb

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


@start_router.callback_query(F.data == 'company_pressed')
async def show_company(callback: CallbackQuery,
                       session_maker: sessionmaker):
    await callback.message.edit_text(text=USERS['company'],
                                     reply_markup=back_menu_kb)
    access = await read_access(callback.from_user.id,
                               session_maker=session_maker)
    if access == 0:
        await update_access(callback.from_user.id,
                            session_maker=session_maker)
    else:
        pass
