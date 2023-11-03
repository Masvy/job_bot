from datetime import datetime

ADMIN: dict[str: str] = {
    'greetings': 'Добро пожаловать в пенель администратора!',
    'select_category': 'Выберите категорию',
    'time': f'Данные актуальны на: {datetime.now(): {"%Y-%m-%d %H:%M:%S"}}',
    'move_dissatisfied': 'Пользователь переведён в категорию "Не устраивает"',
    'move_suits': 'Пользователь переведён в категорию "Устраивает"',
    'move_leads': 'Пользователь переведён в категорию "Лиды"',
    'sent': 'Сообщение отправлено'
}

KEYBOARDS: dict[str: str] = {
    'statistics': 'Статистика',
    'applications': 'Просмотреть заявки',
    'add_vacancies': 'Добавить вакансию',
    'looking_for_work': 'В поисках работы',
    'satisfied_offer': 'Устраивает предложение',
    'back_menu': 'Меню 📋',
    'not_satisfied': 'Не устраивает',
    'send_leads': 'Отправить в лиды',
    'list_leads': 'Список лидов'
}

COMMANDS_LIST: dict[str: str] = {
    '/start': 'Главное меню',
    '/admin': 'Админка'
}
