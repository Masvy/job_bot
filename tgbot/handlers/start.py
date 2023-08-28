from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from lexiocon.user_lexicon import USERS
from keyboards.user_keyboards import main_menu_kb

start_router: Router = Router()


@start_router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(USERS['greetings'],
                         reply_markup=main_menu_kb)
