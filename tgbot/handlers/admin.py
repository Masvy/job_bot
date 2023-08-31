from aiogram.filters import Command, and_f
from aiogram.types import Message
from aiogram import Router
from environs import Env

from lexiocon.admin_lexicon import ADMIN
from filters.admin_filters import IsAdmin

admin_router: Router = Router()

env = Env()
env.read_env()


@admin_router.message(and_f(Command(commands=['admin']),
                            IsAdmin(env('ADMIN_IDS'))))
async def open_admin(message: Message):
    await message.answer(text=ADMIN['greetings'])
