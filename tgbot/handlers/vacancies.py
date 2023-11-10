from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker
from aiogram.filters import StateFilter, or_f, and_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexiocon.user_lexicon import USERS, VACANCIES
from states.users_states import Vacancies, QuestionsVacancies
from keyboards.user_keyboards import company_kb, vacancies_kb2, \
     employments_vac_1, experience_vac, \
     education_vac, back_menu_kb, \
     questions_kb, employments_vac_2, manager_kb, true_false_kb2
from database.users import update_city, update_vacancies, update_employment, \
     update_schedule, update_name, update_age, \
     update_experience, update_education, \
     update_status, update_question, update_access

vacancies_router: Router = Router()


@vacancies_router.callback_query(F.data == 'correct_pressed2')
@vacancies_router.callback_query(F.data == 'vacancies_pressed',
                                 StateFilter(default_state))
async def show_vacancies2(callback: CallbackQuery,
                          state: FSMContext):
    await callback.message.edit_text(text=USERS['interesting_vacancies'])
    await callback.message.edit_reply_markup(reply_markup=vacancies_kb2)
    await state.set_state(Vacancies.vacancies)


@vacancies_router.callback_query(or_f(F.data == 'driver2',
                                      F.data == 'sales_manager2',
                                      F.data == 'salesman_cashier2',
                                      F.data == 'handyman2',
                                      F.data == 'administrator2'))
async def show_description2(callback: CallbackQuery,
                            state: FSMContext,
                            session_maker: sessionmaker):
    """Этот хендлер реагирует на кнопки Водитель/Менеджер по продажам"""
    if callback.data == 'driver2':
        await state.update_data(vacancies='Водитель')
        await update_vacancies(callback.from_user.id, 'Водитель',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['driver'])
        await callback.message.answer(text=USERS['types_employment_1'],
                                      reply_markup=employments_vac_1)
    elif callback.data == 'sales_manager2':
        await state.update_data(vacancies='Менеджер по продажам')
        await update_vacancies(callback.from_user.id, 'Менеджер по продажам',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['sales_manager'])
        await callback.message.answer(text=USERS['types_employment_2'],
                                      reply_markup=employments_vac_2)
    elif callback.data == 'salesman_cashier2':
        await state.update_data(vacancies='Продавец-кассир')
        await update_vacancies(callback.from_user.id, 'Продавец-кассир',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['salesman-cashier'])
        await callback.message.answer(text=USERS['types_employment_3'],
                                      reply_markup=employments_vac_2)

    elif callback.data == 'handyman2':
        await state.update_data(vacancies='Разнорабочий')
        await update_vacancies(callback.from_user.id, 'Разнорабочий',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['handyman'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_vac_2)

    elif callback.data == 'administrator2':
        await state.update_data(vacancies='Администратор')
        await update_vacancies(callback.from_user.id, 'Администратор',
                               session_maker=session_maker)
        await callback.message.edit_text(text=VACANCIES['administrator'])
        await callback.message.answer(text=USERS['types_employment_4'],
                                      reply_markup=employments_vac_2)


@vacancies_router.callback_query(or_f(F.data == 'full_employment_vac',
                                      F.data == 'part-time_employment_vac',
                                      F.data == 'part-time_job_vac'))
async def request_employment2(callback: CallbackQuery,
                              session_maker: sessionmaker,
                              state: FSMContext):
    """
    Этот обработчик реагирует на кнопки Полная занятость/Частичная занятость/Подработка
    """
    if callback.data == 'full_employment_vac':
        await state.update_data(employment='Полная занятость')
        await update_employment(callback.from_user.id, 'Полная занятость',
                                session_maker=session_maker)
        await callback.message.answer(text='Какой график работы вас '
                                      'интересует?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    elif callback.data == 'part-time_employment_vac':
        await state.update_data(employment='Частичная занятость')
        await update_employment(callback.from_user.id, 'Частичная занятость',
                                session_maker=session_maker)
        await callback.message.answer(text='Сколько часов в день вы '
                                      'готовы уделять работе?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    elif callback.data == 'part-time_job_vac':
        await state.update_data(employment='Подработка')
        await update_employment(callback.from_user.id, 'Подработка',
                                session_maker=session_maker)
        await callback.message.answer(text='Сколько часов в день вы '
                                      'готовы уделять работе?\n\nДля отмены '
                                      'анкетирования нажмите /cancel')
    await state.set_state(Vacancies.schedule)


@vacancies_router.message(StateFilter(Vacancies.schedule))
async def request_experience2(message: Message,
                              state: FSMContext):
    await state.update_data(schedule=message.text)
    await message.answer(text='У вас есть опыт работы в данной подобной '
                         'должности?\n\nДля отмены анкетирования нажмите '
                         '/cancel', reply_markup=experience_vac)


@vacancies_router.callback_query(or_f(F.data == 'yes2',
                                      F.data == 'no2'))
async def request_education2(callback: CallbackQuery,
                             state: FSMContext):
    if callback.data == 'yes2':
        await state.update_data(experience='Да')
    elif callback.data == 'no2':
        await state.update_data(experience='Нет')
    await callback.message.edit_text(text='Укажите уровень вашего '
                                          'образования:\n\nДля отмены '
                                          'анкетирования нажмите /cancel',
                                     reply_markup=education_vac)


@vacancies_router.callback_query(or_f(F.data == 'general2',
                                      F.data == 'middle2',
                                      F.data == 'high2'))
async def request_city2(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'general2':
        await state.update_data(education='Общее')
    elif callback.data == 'middle2':
        await state.update_data(education='Среднее')
    elif callback.data == 'high2':
        await state.update_data(education='Высшее')
    await callback.message.edit_text(text=USERS['city_request'])
    await state.set_state(Vacancies.city)


@vacancies_router.message(StateFilter(Vacancies.city),
                          lambda x: x.text.isalpha() and len(x.text) <= 30)
async def request_full_name2(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text='Отлично! Укажите полностью ваше '
                              'ФИО:\n\nДля отмены анкетирования нажмите '
                              '/cancel')
    await state.set_state(Vacancies.name)


@vacancies_router.message(StateFilter(Vacancies.city))
async def wrong_city2(message: Message):
    await message.answer(text=USERS['wrong_city'])


@vacancies_router.message(StateFilter(Vacancies.name),
                          lambda x: len(x.text) <= 60)
async def request_age2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Приятно познакомиться!\nУкажите ваш возраст:'
                              '\n\nДля отмены анкетирования нажмите '
                              '/cancel')
    await state.set_state(Vacancies.age)


@vacancies_router.message(StateFilter(Vacancies.name))
async def wrong_full_name2(message: Message):
    await message.answer(text=USERS['wrong_name'])


@vacancies_router.message(StateFilter(Vacancies.age),
                          lambda x: x.text.isdigit())
async def check_data2(message: Message,
                      state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(text='Проверьте, пожалуйста, корректность введенных '
                              f'данных:\n\nФИО: {data["name"]}\nВозраст: '
                              f'{data["age"]}\nВакансия: {data["vacancies"]}'
                              f'\nВид трудоустройства: {data["employment"]}\n'
                              f'График: {data["schedule"]}\nОпыт работы: '
                              f'{data["experience"]}\nОбразование: '
                              f'{data["education"]}',
                         reply_markup=true_false_kb2)


@vacancies_router.message(StateFilter(Vacancies.age))
async def wrong_age2(message: Message):
    await message.answer(text=USERS['wrong_age'])


@vacancies_router.callback_query(F.data == 'all_right_pressed2')
async def request_question_2(callback: CallbackQuery,
                             state: FSMContext,
                             session_maker: sessionmaker):
    data = await state.get_data()
    await update_name(callback.from_user.id, data['name'], session_maker)
    await update_age(callback.from_user.id,  int(data['age']), session_maker)
    await update_city(callback.from_user.id,  data['city'], session_maker)
    await update_vacancies(callback.from_user.id,  data['vacancies'], session_maker)
    await update_employment(callback.from_user.id,  data['employment'], session_maker)
    await update_schedule(callback.from_user.id,  data['schedule'], session_maker)
    await update_experience(callback.from_user.id,  data['experience'], session_maker)
    await update_education(callback.from_user.id,  data['education'], session_maker)
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
                                  reply_markup=questions_kb)
    await state.clear()


@vacancies_router.callback_query(F.data == 'no_questions_pressed')
async def respond_rejection2(callback: CallbackQuery,
                             session_maker: sessionmaker):
    await update_status(callback.from_user.id, 'Соискатель',
                        session_maker=session_maker)
    await update_access(callback.from_user.id, 2, session_maker=session_maker)
    audio1 = 'CQACAgIAAxkBAAINw2VL291eFejY2098lcX8ufIVO9-PAAJHOwAC4KdYSl2absrsOcxCMwQ'
    audio2 = 'CQACAgIAAxkBAAINx2VL3CQDS6jr9bwYRWeGg3Yjk93DAAJOOwAC4KdYSqxt1Pjo1WJBMwQ'
    audio3 = 'CQACAgIAAxkBAAINxWVL3A4qba4pvTmzro82IdAgsa71AAJMOwAC4KdYSu3FuRIZnwmaMwQ'
    await callback.message.answer_audio(audio1)
    await callback.message.answer_audio(audio2)
    await callback.message.answer_audio(audio3)
    await callback.message.answer(text='Контакты менеджера: @Kanzobozz',
                                  reply_markup=back_menu_kb)


@vacancies_router.callback_query(F.data == 'questions_pressed',
                                 StateFilter(default_state))
async def respond_consent2(callback: CallbackQuery,
                           state: FSMContext):
    await callback.message.edit_text(text='Хорошо, можете задать ваш вопрос:')
    await state.set_state(QuestionsVacancies.question)


@vacancies_router.message(StateFilter(QuestionsVacancies.question))
async def answer_question2(message: Message, state: FSMContext,
                           session_maker: sessionmaker):
    await update_access(message.from_user.id, 2, session_maker=session_maker)
    await update_question(message.from_user.id, message.text,
                          session_maker=session_maker)
    await update_status(message.from_user.id, 'Соискатель',
                        session_maker=session_maker)
    await message.answer(text='Я передам ваш вопрос менеджеру, он свяжется с '
                         'вами в течении 3-х рабочих дней и даст ответ на '
                         'этот и другие вопросы.',
                         reply_markup=manager_kb)
    await state.clear()


# @vacancies_router.callback_query(F.data == 'manager_pressed')
# async def send_audio(callback: CallbackQuery):
#     audio1 = 'CQACAgIAAxkBAAILnmVJElRpB6crdklSXQ3ifivgu2zLAAIkPAAC-MxJSq_nONffv6qDMwQ'
#     audio2 = 'CQACAgIAAxkBAAILqWVJEt3HQBbyGd253sdjYScKysjTAAIqPAAC-MxJSvS8sRmUDLUdMwQ'
#     audio3 = 'CQACAgIAAxkBAAILpWVJErrg081SYocGy38GYRPSWLsjAAInPAAC-MxJSrbSZFmaqzmgMwQ'
#     await callback.message.answer_audio(audio1)
#     await callback.message.answer_audio(audio2)
#     await callback.message.answer_audio(audio3)
#     await callback.message.answer(text='Контакты менеджера: @GroupSwit',
#                                   reply_markup=back_menu_kb)
