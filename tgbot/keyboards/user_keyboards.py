from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexiocon.user_lexicon import KEYBOARDS

# Создал объекты клавиатуры
main_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['vacancies'],
                                 callback_data='vacancies_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['company'],
                                 callback_data='company_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['employment'],
                                 callback_data='employment_pressed')
        ]
    ]
)
