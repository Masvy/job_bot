from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexiocon.user_lexicon import KEYBOARDS

# Создал объекты клавиатуры
main_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['about_company'],
                              callback_data='company_pressed')],
        [InlineKeyboardButton(text=KEYBOARDS['vacancies'],
                              callback_data='vacancies_pressed')],
        [InlineKeyboardButton(text=KEYBOARDS['employment'],
                              callback_data='employment_pressed')]
        ]
)

back_menu_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['back_menu'],
                              callback_data='back_menu_pressed')]
    ]
)

consent_questionnaire_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='agreement_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='refusal_pressed')
        ]
    ]
)

yes_or_no_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='yes_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='refusal_pressed')
        ]
    ]
)

true_false_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['all_right'],
                                 callback_data='all_right_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['correct'],
                                 callback_data='correct_pressed')
        ]
    ]
)

company_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['show_vacancies'],
                                 callback_data='show_vacancies_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['back_menu'],
                                 callback_data='back_menu_pressed')
        ]
    ]
)

vacancies_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Водитель',
                              callback_data='Водитель')]
    ]
)

employments_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Полная занятость',
                              callback_data='Полная занятость')]
    ]
)

experience_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='Да'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='Нет')
        ]
    ]
)

education_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['general'],
                                 callback_data='Общее'),
            InlineKeyboardButton(text=KEYBOARDS['middle'],
                                 callback_data='Среднее'),
            InlineKeyboardButton(text=KEYBOARDS['high'],
                                 callback_data='Высшее')
        ]
    ]
)

questions_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='questions_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no_questions_pressed')
        ]
    ]
)
