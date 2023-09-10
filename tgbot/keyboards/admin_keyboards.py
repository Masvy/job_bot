from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

from lexiocon.admin_lexicon import KEYBOARDS

# Создал объекты клавиатуры
admin_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['statistics'],
                              callback_data='statistics_pressed')],
        [InlineKeyboardButton(text=KEYBOARDS['applications'],
                              callback_data='applications_pressed')]
        ]
)

category_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['looking_for_work'],
                                 callback_data='looking_for_work_pressed')
        ],
        [
            InlineKeyboardButton(text=KEYBOARDS['satisfied_offer'],
                                 callback_data='satisfied_offer_pressed')
        ],
        [
            InlineKeyboardButton(text=KEYBOARDS['list_leads'],
                                 callback_data='list_leads_pressed')
        ]
    ]
)

manipuations_kb_1: InlineKeyboardButton = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Обновить список',
                                 callback_data='update_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['back_menu'],
                                 callback_data='back_menu_admin_pressed')
        ]
    ]
)

manipuations_kb_2: InlineKeyboardButton = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Обновить список',
                                 callback_data='update_pressed_2'),
            InlineKeyboardButton(text=KEYBOARDS['back_menu'],
                                 callback_data='back_menu_admin_pressed')
        ]
    ]
)

manipuations_kb_3: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['back_menu'],
                              callback_data='back_menu_admin_pressed')]
    ]
)


class MyCallbackFactory(CallbackData, prefix='any'):
    user_id: int
    subcategory: int


def function(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='❌',
                                     callback_data=MyCallbackFactory(
                                         user_id=user_id,
                                         subcategory=1).pack()),
                InlineKeyboardButton(text='✅',
                                     callback_data=MyCallbackFactory(
                                         user_id=user_id,
                                         subcategory=2).pack())
            ]
        ]
    )


def function2(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=KEYBOARDS['send_leads'],
                                  callback_data=MyCallbackFactory(
                                  user_id=user_id,
                                  subcategory=3).pack())]
        ]
    )
