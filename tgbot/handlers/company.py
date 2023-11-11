from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker
from aiogram.filters import StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexiocon.user_lexicon import USERS, VACANCIES
from states.users_states import Company, QuestionsCompany
from keyboards.user_keyboards import company_kb, vacancies_kb1, \
     employments_comp_1, experience_com, \
     education_com, back_menu_kb, \
     questions_com, employments_comp_2, true_false_kb1
from database.users import update_access, update_city, \
     update_vacancies, update_employment, \
     update_schedule, update_name, update_age, \
     update_experience, update_education, \
     update_status, update_question, read_access

company_router: Router = Router()


@company_router.callback_query(F.data == 'company_pressed')
async def show_company(callback: CallbackQuery):
    """Этот обработчик реагирует на кнопку О компании"""
    await callback.message.edit_text(text=USERS['company'])
    await callback.message.answer(text=USERS['jobs_in_city'],
                                  reply_markup=company_kb)


@company_router.callback_query(F.data == 'correct_pressed1')
@company_router.callback_query(F.data == 'show_vacancies_pressed',
                               StateFilter(default_state))
async def request_city1(callback: CallbackQuery,
                        state: FSMContext,):
    """Этот обработчик реагирует на кнопку: Просмотреть вакансии"""
    await callback.message.edit_text(text=USERS['city_input_2'])
    print(callback.message.text)
    await state.set_state(Company.city)


@company_router.message(StateFilter(Company.city),
                        lambda x: len(x.text) <= 30)
async def show_vacancies(message: Message,
                         state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text=USERS['interesting_vacancies'],
                         reply_markup=vacancies_kb1)


@company_router.message(StateFilter(Company.city))
async def wrong_cities1(message: Message):
    await message.answer(text=USERS['wrong_city'])


@company_router.callback_query(or_f(F.data == 'driver1',
                                    F.data == 'sales_manager1',
                                    F.data == 'salesman_cashier1',
                                    F.data == 'handyman1',
                                    F.data == 'administrator1'))
async def show_description(callback: CallbackQuery,
                           state: FSMContext):
    """Этот обработчик реагирует на кнопки Водитель/Менеджер по продажам"""
    if callback.data == 'driver1':
        await state.update_data(vacancies='Водитель')
        await callback.message.edit_text(text=VACANCIES['driver'])
        await callback.message.answer(text=USERS['types_employment_1'],
                                      reply_markup=employments_comp_1)
    elif callback.data == 'sales_manager1':
        await state.update_data(vacancies='Менеджер по продажам')
        await callback.message.edit_text(text=VACANCIES['sales_manager'])
        await callback.message.answer(text=USERS['types_employment_2'],
                                      reply_markup=employments_comp_2)
    elif callback.data == 'salesman_cashier1':
        await state.update_data(vacancies='Продавец-кассир')
        await callback.message.edit_text(text=VACANCIES['salesman-cashier'])
        await callback.message.answer(text=USERS['types_employment_3'],
                                      reply_markup=employments_comp_2)

    elif callback.data == 'handyman1':
        await state.update_data(vacancies='Разнорабочий')
        await callback.message.edit_text(text=VACANCIES['handyman'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_comp_2)

    elif callback.data == 'administrator1':
        await state.update_data(vacancies='Администратор')
        await callback.message.edit_text(text=VACANCIES['administrator'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_comp_2)


@company_router.callback_query(or_f(F.data == 'full_employment_comp',
                                    F.data == 'part-time_employment_comp',
                                    F.data == 'part-time_job_comp'))
async def request_employment1(callback: CallbackQuery,
                              state: FSMContext):
    """
    Этот обработчик реагирует на кнопки Полная занятость/Частичная занятость/Подработка
    """
    if callback.data == 'full_employment_comp':
        await state.update_data(employment='Полная занятость')
        await callback.message.answer(text='Какой график работы вас '
                                      'интересует?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    elif callback.data == 'part-time_employment_comp':
        await state.update_data(employment='Частичная занятость')
        await callback.message.answer(text='Сколько часов в день вы '
                                      'готовы уделять работе?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    elif callback.data == 'part-time_job_comp':
        await state.update_data(employment='Подработка')
        await callback.message.answer(text='Сколько часов в день вы '
                                      'готовы уделять работе?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    await state.set_state(Company.schedule)


@company_router.message(StateFilter(Company.schedule))
async def request_full_name1(message: Message,
                             state: FSMContext):
    await state.update_data(schedule=message.text)
    await message.answer(text='Отлично! Чтобы ускорить процесс '
                              'трудоустройства, вы можете заполнить '
                              'анкету сейчас. Укажите полностью ваше '
                              'ФИО:\n\nДля отмены анкетирования нажмите '
                              '/cancel')
    await state.set_state(Company.name)


@company_router.message(StateFilter(Company.name),
                        lambda x: len(x.text) <= 60)
async def request_age1(message: Message,
                       state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Приятно познакомиться!\nУкажите '
                         'ваш возраст:\n\nДля отмены анкетирования '
                         'нажмите /cancel')
    await state.set_state(Company.age)


@company_router.message(StateFilter(Company.name))
async def wrong_name1(message: Message):
    await message.answer(text=USERS['wrong_name'])


@company_router.message(StateFilter(Company.age),
                        lambda x: x.text.isdigit())
async def request_experience1(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(text='У вас есть опыт работы в данной подобной '
                         'должности?\n\nДля отмены анкетирования нажмите '
                         '/cancel', reply_markup=experience_com)


@company_router.message(StateFilter(Company.age))
async def incorrect_age(message: Message):
    await message.answer(text=USERS['wrong_age'])


@company_router.callback_query(or_f(F.data == 'yes1',
                                    F.data == 'no1'))
async def request_education1(callback: CallbackQuery,
                             state: FSMContext):
    if callback.data == 'yes1':
        await state.update_data(experience='Да')
    elif callback.data == 'no1':
        await state.update_data(experience='Нет')
    await callback.message.edit_text(text='Укажите уровень вашего '
                                     'образования:\n\nДля отмены '
                                     'анкетирования нажмите /cancel',
                                     reply_markup=education_com)


@company_router.callback_query(or_f(F.data == 'general1',
                                    F.data == 'middle1',
                                    F.data == 'high1'))
async def check_data1(callback: CallbackQuery,
                      state: FSMContext):
    if callback.data == 'general1':
        await state.update_data(education='Общее')
    elif callback.data == 'middle1':
        await state.update_data(education='Среднее')
    elif callback.data == 'high1':
        await state.update_data(education='Высшее')
    data = await state.get_data()
    await callback.message.answer(text='Проверьте, пожалуйста, корректность введенных '
                                  f'данных:\n\nФИО: {data["name"]}\nВозраст: '
                                  f'{data["age"]}\nВакансия: {data["vacancies"]}'
                                  f'\nВид трудоустройства: {data["employment"]}\n'
                                  f'График: {data["schedule"]}\nОпыт работы: '
                                  f'{data["experience"]}\nОбразование: '
                                  f'{data["education"]}',
                                  reply_markup=true_false_kb1)


@company_router.callback_query(F.data == 'all_right_pressed1')
async def request_question_3(callback: CallbackQuery,
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
                                  reply_markup=questions_com)
    await state.clear()


@company_router.callback_query(F.data == 'no_questions1')
async def respond_rejection(callback: CallbackQuery,
                            session_maker: sessionmaker):
    await update_status(callback.from_user.id, status='Соискатель',
                        session_maker=session_maker)
    access = await read_access(callback.from_user.id,
                               session_maker=session_maker)
    if access < 2:
        await update_access(callback.from_user.id, access=1, session_maker=session_maker)
    audio1 = 'CQACAgIAAxkBAAMGZU-jkgcUeohBWIATCkW3bRTd6jMAAls4AAIS0IBKlYX_d9vPDrkzBA'
    audio2 = 'CQACAgIAAxkBAAMIZU-j_tmE5m7mM7NlVynCoHFMpTIAAmY4AAIS0IBKEXq1Od5m9lQzBA'
    audio3 = 'CQACAgIAAxkBAAMKZU-kXbTai7GHxoysqCFCH1X-A-8AAmg4AAIS0IBK5ZbdOeV1gM4zBA'
    await callback.message.answer_audio(audio1)
    await callback.message.answer_audio(audio2)
    await callback.message.answer_audio(audio3)
    await callback.message.answer(text='Контакты менеджера: @Kanzobozz',
                                  reply_markup=back_menu_kb)


@company_router.callback_query(F.data == 'questions1',
                               StateFilter(default_state))
async def respond_consent(callback: CallbackQuery,
                          state: FSMContext):
    audio1 = 'CQACAgIAAxkBAAMGZU-jkgcUeohBWIATCkW3bRTd6jMAAls4AAIS0IBKlYX_d9vPDrkzBA'
    audio2 = 'CQACAgIAAxkBAAMIZU-j_tmE5m7mM7NlVynCoHFMpTIAAmY4AAIS0IBKEXq1Od5m9lQzBA'
    audio3 = 'CQACAgIAAxkBAAMKZU-kXbTai7GHxoysqCFCH1X-A-8AAmg4AAIS0IBK5ZbdOeV1gM4zBA'
    await callback.message.answer_audio(audio1)
    await callback.message.answer_audio(audio2)
    await callback.message.answer_audio(audio3)
    await callback.message.answer(text='Хорошо, можете задать ваш вопрос:')
    await state.set_state(QuestionsCompany.question)


@company_router.message(StateFilter(QuestionsCompany.question))
async def answer_question(message: Message, state: FSMContext,
                          session_maker: sessionmaker):
    await state.clear()
    access = await read_access(message.from_user.id,
                               session_maker=session_maker)
    if access < 2:
        await update_access(message.from_user.id, access=1, session_maker=session_maker)
    await update_question(message.from_user.id, message.text,
                          session_maker=session_maker)
    await update_status(message.from_user.id, status='Соискатель',
                        session_maker=session_maker)
    await message.answer(text='Контакты менеджера: @Kanzobozz')
    await message.answer(text='Я передам ваш вопрос менеджеру, он свяжется с '
                         'вами в течении 3-х рабочих дней и даст ответ на '
                         'этот и другие вопросы.',
                         reply_markup=back_menu_kb)
