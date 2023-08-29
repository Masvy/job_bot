from aiogram import Router, F
from aiogram.types import CallbackQuery

from lexiocon.user_lexicon import USERS
from keyboards.user_keyboards import back_menu_kb, consent_questionnaire_kb, \
                                     yes_or_no_kb

employment_router: Router = Router()


@employment_router.callback_query(F.data == 'employment_pressed')
async def employ(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['employment_info'],
                                     reply_markup=consent_questionnaire_kb)


@employment_router.callback_query(F.data == 'agreement_pressed')
async def warn_user(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['agreement'],
                                     reply_markup=yes_or_no_kb)


@employment_router.callback_query(F.data == 'yes_pressed')
async def request_name(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['name_request'])


@employment_router.callback_query(F.data == 'refusal_pressed')
async def thank_contacting(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['refusal'],
                                     reply_markup=back_menu_kb)
