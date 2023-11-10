from aiogram.types import Message
from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from sqlalchemy.orm import sessionmaker
from aiogram.fsm.context import FSMContext

from lexiocon.user_lexicon import USERS
from keyboards.user_keyboards import main_menu_kb_1, main_menu_kb_2, \
     main_menu_kb_3, main_menu_kb_4, back_menu_kb
from database.users import read_access

start_router: Router = Router()


@start_router.callback_query(F.data == 'back_menu_pressed')
@start_router.message(CommandStart())
async def start_bot(update: types.update,
                    session_maker: sessionmaker):
    access = await read_access(update.from_user.id,
                               session_maker=session_maker)
    if isinstance(update, types.CallbackQuery):
        await update.message.edit_text(text=USERS['main_manu'],
                                       reply_markup=main_menu_kb_4)

    elif isinstance(update, types.Message):
        await update.answer(text=USERS['greetings'],
                            reply_markup=main_menu_kb_4)


@start_router.message(Command(commands='cancel'))
async def cancel_we(message: Message,
                    state: FSMContext):
    await message.answer(text='Анкетирование отменено',
                         reply_markup=back_menu_kb)
    await state.clear()


@start_router.message(F.audio)
async def get_id(msg: Message):
    file_id = msg.audio.file_id
    await msg.answer(file_id)
