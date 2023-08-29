from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexiocon.user_lexicon import KEYBOARDS

# Создал объекты клавиатуры
main_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['vacancies'],
                                 callback_data='vacancies_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['about_company'],
                                 callback_data='company_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['employment'],
                                 callback_data='employment_pressed')
        ]
    ]
)

back_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['back_menu'],
                              callback_data='back_menu_pressed')]
    ]
)

yes_or_no_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='yes_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no_pressed')
        ]
    ]
)
