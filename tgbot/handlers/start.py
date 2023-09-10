from aiogram import Router, F, types
from aiogram.filters import CommandStart
from sqlalchemy.orm import sessionmaker

from lexiocon.user_lexicon import USERS
from keyboards.user_keyboards import main_menu_kb_1, main_menu_kb_2, \
                                     main_menu_kb_3
from database.users import read_access

start_router: Router = Router()


@start_router.callback_query(F.data == 'back_menu_pressed')
@start_router.message(CommandStart())
async def start_bot(update: types.update,
                    session_maker: sessionmaker):
    access = await read_access(update.from_user.id,
                               session_maker=session_maker)
    if access == 0:
        if isinstance(update, types.CallbackQuery):
            await update.message.edit_text(text=USERS['main_manu'],
                                           reply_markup=main_menu_kb_1)
        elif isinstance(update, types.Message):
            await update.answer(text=USERS['greetings'],
                                reply_markup=main_menu_kb_1)
    elif access == 1:
        if isinstance(update, types.CallbackQuery):
            await update.message.edit_text(text=USERS['main_manu'],
                                           reply_markup=main_menu_kb_2)
        elif isinstance(update, types.Message):
            await update.answer(text=USERS['greetings'],
                                reply_markup=main_menu_kb_2)
    else:
        if isinstance(update, types.CallbackQuery):
            await update.message.edit_text(text=USERS['main_manu'],
                                           reply_markup=main_menu_kb_3)
        elif isinstance(update, types.Message):
            await update.answer(text=USERS['greetings'],
                                reply_markup=main_menu_kb_3)
