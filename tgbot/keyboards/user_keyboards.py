from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexiocon.user_lexicon import KEYBOARDS

# Создал объекты клавиатуры
main_menu_kb_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['about_company'],
                              callback_data='company_pressed')]
    ]
)

main_menu_kb_2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['about_company'],
                              callback_data='company_pressed')],
        [InlineKeyboardButton(text=KEYBOARDS['vacancies'],
                              callback_data='vacancies_pressed')]
    ]
)

main_menu_kb_3: InlineKeyboardMarkup = InlineKeyboardMarkup(
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
        [InlineKeyboardButton(text=KEYBOARDS['driver'],
                              callback_data='Водитель')],
        [InlineKeyboardButton(text=KEYBOARDS['sales_manager'],
                              callback_data='Менеджер по продажам')],
        [InlineKeyboardButton(text=KEYBOARDS['salesman-cashier'],
                              callback_data='Продавец-кассир')],
        [InlineKeyboardButton(text=KEYBOARDS['handyman'],
                              callback_data='Разнорабочий')]
    ]
)

employments_kb_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='Полная занятость')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_employment'],
                              callback_data='Частичная занятость')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='Подработка')]
    ]
)

employments_kb_2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='Полная занятость')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='Подработка')]
    ]
)

schedule_1_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['2/2'],
                                 callback_data='2/2'),
            InlineKeyboardButton(text=KEYBOARDS['3/3'],
                                 callback_data='3/3'),
            InlineKeyboardButton(text=KEYBOARDS['5/2'],
                                 callback_data='5/2')
        ]
    ]
)

schedule_2_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['3-4'],
                                 callback_data='3-4'),
            InlineKeyboardButton(text=KEYBOARDS['5-6'],
                                 callback_data='5-6')
        ]
    ]
)

schedule_3_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['1-2'],
                                 callback_data='1-2'),
            InlineKeyboardButton(text=KEYBOARDS['3-4'],
                                 callback_data='3-4')
        ]
    ]
)

schedule_4_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['2/2'],
                                 callback_data='2/2'),
            InlineKeyboardButton(text=KEYBOARDS['5/2'],
                                 callback_data='5/2')
        ]
    ]
)

schedule_5_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['2-4'],
                                 callback_data='2-4')
        ]
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
