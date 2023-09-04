from aiogram import Router, F, types
from aiogram.filters import CommandStart

from lexiocon.user_lexicon import USERS
from keyboards.user_keyboards import main_menu_kb

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
