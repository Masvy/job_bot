from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker
from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexiocon.user_lexicon import USERS, VACANCIES
from states.users_states import Employments, QuestionsEmployments
from keyboards.user_keyboards import company_kb, vacancies_kb3, \
    employments_emp_1, experience_emp, \
    education_emp, back_menu_kb, \
    questions_emp, employments_emp_2, true_false_kb3
from database.users import update_city, update_vacancies, update_employment, \
     update_schedule, update_name, update_age, \
     update_experience, update_education, \
     update_status, update_question

employment_router: Router = Router()


@employment_router.callback_query(F.data == 'employment_pressed')
async def employ(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['jobs_in_city'],
                                     reply_markup=company_kb)


@employment_router.callback_query(F.data == 'correct_pressed3')
@employment_router.callback_query(F.data == 'show_vacancies_pressed',
                                  StateFilter(default_state))
async def request_city_3(callback: CallbackQuery,
                         state: FSMContext):
    await callback.message.edit_text(text=USERS['city_input_2'])
    await state.set_state(Employments.city)


@employment_router.message(StateFilter(Employments.city),
                           lambda x: len(x.text) <= 30)
async def show_vacancies_3(message: Message,
                           state: FSMContext,
                           session_maker: sessionmaker):
    await state.update_data(city=message.text)
    await update_city(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text=USERS['interesting_vacancies'],
                         reply_markup=vacancies_kb3)
    await state.clear()


@employment_router.message(StateFilter(Employments.city))
async def wrong_cities3(message: Message):
    await message.answer(text=USERS['wrong_city'])


@employment_router.callback_query(or_f(F.data == 'driver3',
                                       F.data == 'sales_manager3',
                                       F.data == 'salesman_cashier3',
                                       F.data == 'handyman3',
                                       F.data == 'administrator3'))
async def show_description3(callback: CallbackQuery,
                            state: FSMContext,
                            session_maker: sessionmaker):
    """Этот хендлер реагирует на кнопки Водитель/Менеджер по продажам"""
    if callback.data == 'driver3':
        await state.update_data(vacancies='Водитель')
        await update_vacancies(callback.from_user.id, vacancies='Водитель',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['driver'])
        await callback.message.answer(text=USERS['types_employment_1'],
                                      reply_markup=employments_emp_1)
    elif callback.data == 'sales_manager3':
        await state.update_data(vacancies='Менеджер по продажам')
        await update_vacancies(callback.from_user.id, vacancies='Менеджер по продажам',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['sales_manager'])
        await callback.message.answer(text=USERS['types_employment_2'],
                                      reply_markup=employments_emp_2)
    elif callback.data == 'salesman_cashier3':
        await state.update_data(vacancies='Продавец-кассир')
        await update_vacancies(callback.from_user.id, vacancies='Продавец-кассир',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['salesman-cashier'])
        await callback.message.answer(text=USERS['types_employment_3'],
                                      reply_markup=employments_emp_2)

    elif callback.data == 'handyman3':
        await state.update_data(vacancies='Разнорабочий')
        await update_vacancies(callback.from_user.id, vacancies='Разнорабочий',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['handyman'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_emp_2)

    elif callback.data == 'administrator3':
        await state.update_data(vacancies='Администратор')
        await update_vacancies(callback.from_user.id, vacancies='Администратор',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['administrator'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_emp_2)


@employment_router.callback_query(or_f(F.data == 'full_employment_emp',
                                       F.data == 'part-time_employment_emp',
                                       F.data == 'part-time_job_emp'))
async def request_employment3(callback: CallbackQuery,
                              session_maker: sessionmaker,
                              state: FSMContext):
    """
    Этот обработчик реагирует на кнопки Полная занятость/Частичная занятость/Подработка
    """
    if callback.data == 'full_employment_emp':
        await state.update_data(employment='Полная занятость')
        await update_employment(callback.from_user.id, employment='Полная занятость',
                                session_maker=session_maker)
        await callback.message.answer(text='Какой график работы вас '
                                      'интересует?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    elif callback.data == 'part-time_employment_emp':
        await state.update_data(employment='Частичная занятость')
        await update_employment(callback.from_user.id, employment='Частичная занятость',
                                session_maker=session_maker)
        await callback.message.answer(text='Сколько часов в день вы '
                                      'готовы уделять работе?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    elif callback.data == 'part-time_job_emp':
        await state.update_data(employment='Подработка')
        await update_employment(callback.from_user.id, employment='Подработка',
                                session_maker=session_maker)
        await callback.message.answer(text='Сколько часов в день вы '
                                      'готовы уделять работе?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    await state.set_state(Employments.schedule)


@employment_router.message(StateFilter(Employments.schedule))
async def request_full_name3(message: Message,
                             state: FSMContext,
                             session_maker: sessionmaker):
    await state.update_data(schedule=message.text)
    await update_schedule(message.from_user.id, message.text,
                          session_maker=session_maker)
    await message.answer(text='Отлично! Чтобы ускорить процесс '
                              'трудоустройства, вы можете заполнить '
                              'анкету сейчас. Укажите полностью ваше '
                              'ФИО:\n\nДля отмены анкетирования нажмите '
                              '/cancel')
    await state.set_state(Employments.name)


@employment_router.message(StateFilter(Employments.name),
                           lambda x: len(x.text) <= 60)
async def request_age_3(message: Message, state: FSMContext,
                        session_maker: sessionmaker):
    await state.update_data(name=message.text)
    await update_name(message.from_user.id, message.text,
                      session_maker=session_maker)
    await message.answer(text='Приятно познакомиться!\nУкажите '
                         'ваш возраст:\n\nДля отмены анкетирования '
                         'нажмите /cancel')
    await state.set_state(Employments.age)


@employment_router.message(StateFilter(Employments.name))
async def incorrect_name_3(message: Message):
    await message.answer(text=USERS['wrong_name'])


@employment_router.message(StateFilter(Employments.age),
                           lambda x: x.text.isdigit())
async def request_experience_3(message: Message,
                               state: FSMContext,
                               session_maker: sessionmaker):
    await state.update_data(age=message.text)
    await update_age(message.from_user.id, int(message.text),
                     session_maker=session_maker)
    await message.answer(text='У вас есть опыт работы в данной подобной '
                         'должности?\n\nДля отмены анкетирования нажмите '
                         '/cancel', reply_markup=experience_emp)


@employment_router.message(StateFilter(Employments.age))
async def incorrect_age_3(message: Message):
    await message.answer(text=USERS['wrong_age'])


@employment_router.callback_query(or_f(F.data == 'yes3',
                                       F.data == 'no3'))
async def request_education_3(callback: CallbackQuery,
                              state: FSMContext,
                              session_maker: sessionmaker):
    if callback.data == 'yes3':
        await state.update_data(experience='Да')
        await update_experience(callback.from_user.id, experience='Да',
                                session_maker=session_maker)
    elif callback.data == 'no3':
        await state.update_data(experience='Нет')
        await update_experience(callback.from_user.id, experience='Нет',
                                session_maker=session_maker)
    await callback.message.edit_text(text='Укажите уровень вашего '
                                     'образования:\n\nДля отмены '
                                     'анкетирования нажмите /cancel',
                                     reply_markup=education_emp)


@employment_router.callback_query(or_f(F.data == 'general3',
                                       F.data == 'middle3',
                                       F.data == 'high3'))
async def check_data3(callback: CallbackQuery,
                      state: FSMContext):
    if callback.data == 'general3':
        await state.update_data(education='Общее')
    elif callback.data == 'middle3':
        await state.update_data(education='Среднее')
    elif callback.data == 'high3':
        await state.update_data(education='Высшее')
    data = await state.get_data()
    await callback.message.answer(text='Проверьте, пожалуйста, корректность введенных '
                                  f'данных:\n\nФИО: {data["name"]}\nВозраст: '
                                  f'{data["age"]}\nВакансия: {data["vacancies"]}'
                                  f'\nВид трудоустройства: {data["employment"]}\n'
                                  f'График: {data["schedule"]}\nОпыт работы: '
                                  f'{data["experience"]}\nОбразование: '
                                  f'{data["education"]}',
                                  reply_markup=true_false_kb3)


@employment_router.callback_query(F.data == 'all_right_pressed3')
async def request_question_2(callback: CallbackQuery,
                             state: FSMContext,
                             session_maker: sessionmaker):
    data = await state.get_data()
    await update_name(callback.from_user.id, data['name'], session_maker)
    await update_age(callback.from_user.id, int(data['age']), session_maker)
    await update_city(callback.from_user.id, data['city'], session_maker)
    await update_vacancies(callback.from_user.id, data['vacancies'], session_maker)
    await update_employment(callback.from_user.id, data['employment'], session_maker)
    await update_schedule(callback.from_user.id, data['schedule'], session_maker)
    await update_experience(callback.from_user.id, data['experience'], session_maker)
    await update_education(callback.from_user.id, data['education'], session_maker)
    await callback.message.edit_text(text='Первичная анкета заполнена.'
                                     'В течении 3 дней менеджер рассмотрит '
                                     'вашу заявку и даст ответ по '
                                     'трудоустройству. А так же назначит '
                                     'день встречи для обсуждения деталей '
                                     'работы.')
    await callback.message.answer(text='На собеседование возьмите с собой '
                                       'следующие документы:\n\t📌 Паспорт'
                                       ';\n\t📌 ИНН;\n\t📌 Документ, подтверждающий '
                                       'образование.\nПосле собеседования '
                                       'менеджер предложит вам сразу заключить '
                                       'трудовой договор/ГПХ и приступить к работе '
                                       'на следующий день.\n\nУ вас остались '
                                       'какие-нибудь вопросы?',
                                  reply_markup=questions_emp)
    await state.clear()


@employment_router.callback_query(F.data == 'no_questions3')
async def respond_rejection3(callback: CallbackQuery,
                             session_maker: sessionmaker):
    await update_status(callback.from_user.id, status='Соискатель',
                        session_maker=session_maker)
    audio1 = 'CQACAgIAAxkBAAMGZU-jkgcUeohBWIATCkW3bRTd6jMAAls4AAIS0IBKlYX_d9vPDrkzBA'
    audio2 = 'CQACAgIAAxkBAAMIZU-j_tmE5m7mM7NlVynCoHFMpTIAAmY4AAIS0IBKEXq1Od5m9lQzBA'
    audio3 = 'CQACAgIAAxkBAAMKZU-kXbTai7GHxoysqCFCH1X-A-8AAmg4AAIS0IBK5ZbdOeV1gM4zBA'
    await callback.message.answer_audio(audio1)
    await callback.message.answer_audio(audio2)
    await callback.message.answer_audio(audio3)
    await callback.message.answer(text='Контакты менеджера: @Kanzobozz',
                                  reply_markup=back_menu_kb)


@employment_router.callback_query(F.data == 'questions3',
                                  StateFilter(default_state))
async def respond_consent_3(callback: CallbackQuery,
                            state: FSMContext):
    audio1 = 'CQACAgIAAxkBAAMGZU-jkgcUeohBWIATCkW3bRTd6jMAAls4AAIS0IBKlYX_d9vPDrkzBA'
    audio2 = 'CQACAgIAAxkBAAMIZU-j_tmE5m7mM7NlVynCoHFMpTIAAmY4AAIS0IBKEXq1Od5m9lQzBA'
    audio3 = 'CQACAgIAAxkBAAMKZU-kXbTai7GHxoysqCFCH1X-A-8AAmg4AAIS0IBK5ZbdOeV1gM4zBA'
    await callback.message.answer_audio(audio1)
    await callback.message.answer_audio(audio2)
    await callback.message.answer_audio(audio3)
    await callback.message.answer(text='Хорошо, можете задать ваш вопрос:')
    await state.set_state(QuestionsEmployments.question)


@employment_router.message(StateFilter(QuestionsEmployments.question))
async def answer_question3(message: Message, state: FSMContext,
                           session_maker: sessionmaker):
    await state.clear()
    await update_question(message.from_user.id, message.text,
                          session_maker=session_maker)
    await update_status(message.from_user.id, status='Соискатель',
                        session_maker=session_maker)
    await message.answer(text='Контакты менеджера: @Kanzobozz')
    await message.answer(text='Я передам ваш вопрос менеджеру, он свяжется с '
                         'вами в течении 3-х рабочих дней и даст ответ на '
                         'этот и другие вопросы.',
                         reply_markup=back_menu_kb)
