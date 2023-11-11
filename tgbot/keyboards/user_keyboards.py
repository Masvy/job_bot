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

true_false_kb1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['all_right'],
                                 callback_data='all_right_pressed1'),
            InlineKeyboardButton(text=KEYBOARDS['correct'],
                                 callback_data='correct_pressed1')
        ]
    ]
)

true_false_kb2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['all_right'],
                                 callback_data='all_right_pressed2'),
            InlineKeyboardButton(text=KEYBOARDS['correct'],
                                 callback_data='correct_pressed2')
        ]
    ]
)

true_false_kb3: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['all_right'],
                                 callback_data='all_right_pressed3'),
            InlineKeyboardButton(text=KEYBOARDS['correct'],
                                 callback_data='correct_pressed3')
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

vacancies_kb1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['driver'],
                              callback_data='driver1')],
        [InlineKeyboardButton(text=KEYBOARDS['sales_manager'],
                              callback_data='sales_manager1')],
        [InlineKeyboardButton(text=KEYBOARDS['salesman-cashier'],
                              callback_data='salesman_cashier1')],
        [InlineKeyboardButton(text=KEYBOARDS['handyman'],
                              callback_data='handyman1')],
        [InlineKeyboardButton(text=KEYBOARDS['administrator'],
                              callback_data='administrator1')]
    ]
)

vacancies_kb2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['driver'],
                              callback_data='driver2')],
        [InlineKeyboardButton(text=KEYBOARDS['sales_manager'],
                              callback_data='sales_manager2')],
        [InlineKeyboardButton(text=KEYBOARDS['salesman-cashier'],
                              callback_data='salesman_cashier2')],
        [InlineKeyboardButton(text=KEYBOARDS['handyman'],
                              callback_data='handyman2')],
        [InlineKeyboardButton(text=KEYBOARDS['administrator'],
                              callback_data='administrator2')]
    ]
)

vacancies_kb3: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['driver'],
                              callback_data='driver3')],
        [InlineKeyboardButton(text=KEYBOARDS['sales_manager'],
                              callback_data='sales_manager3')],
        [InlineKeyboardButton(text=KEYBOARDS['salesman-cashier'],
                              callback_data='salesman_cashier3')],
        [InlineKeyboardButton(text=KEYBOARDS['handyman'],
                              callback_data='handyman3')],
        [InlineKeyboardButton(text=KEYBOARDS['administrator'],
                              callback_data='administrator3')]
    ]
)

employments_comp_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='full_employment_comp')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_employment'],
                              callback_data='part-time_employment_comp')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='part-time_job_comp')]
    ]
)

employments_comp_2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='full_employment_comp')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='part-time_job_comp')]
    ]
)

employments_vac_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='full_employment_vac')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_employment'],
                              callback_data='part-time_employment_vac')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='part-time_job_vac')]
    ]
)

employments_vac_2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='full_employment_vac')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='part-time_job_vac')]
    ]
)

employments_emp_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='full_employment_emp')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_employment'],
                              callback_data='part-time_employment_emp')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='part-time_job_emp')]
    ]
)

employments_emp_2: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['full_employment'],
                              callback_data='full_employment_emp')],
        [InlineKeyboardButton(text=KEYBOARDS['part-time_job'],
                              callback_data='part-time_job_emp')]
    ]
)

experience_com: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='yes1'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no1')
        ]
    ]
)

experience_vac: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='yes2'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no2')
        ]
    ]
)

experience_emp: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='yes3'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no3')
        ]
    ]
)

education_com: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['general'],
                                 callback_data='general1'),
            InlineKeyboardButton(text=KEYBOARDS['middle'],
                                 callback_data='middle1'),
            InlineKeyboardButton(text=KEYBOARDS['high'],
                                 callback_data='high1')
        ]
    ]
)

education_vac: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['general'],
                                 callback_data='general2'),
            InlineKeyboardButton(text=KEYBOARDS['middle'],
                                 callback_data='middle2'),
            InlineKeyboardButton(text=KEYBOARDS['high'],
                                 callback_data='high2')
        ]
    ]
)

education_emp: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['general'],
                                 callback_data='general3'),
            InlineKeyboardButton(text=KEYBOARDS['middle'],
                                 callback_data='middle3'),
            InlineKeyboardButton(text=KEYBOARDS['high'],
                                 callback_data='high3')
        ]
    ]
)

questions_com: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='questions1'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no_questions1')
        ]
    ]
)

questions_vac: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='questions2'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no_questions2')
        ]
    ]
)

questions_emp: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['yes'],
                                 callback_data='questions3'),
            InlineKeyboardButton(text=KEYBOARDS['no'],
                                 callback_data='no_questions3')
        ]
    ]
)
