from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexiocon.admin_lexicon import KEYBOARDS

# Создал объекты клавиатуры
admin_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['statistics'],
                                 callback_data='statistics_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['applications'],
                                 callback_data='applications_pressed')
        ]
    ]
)
