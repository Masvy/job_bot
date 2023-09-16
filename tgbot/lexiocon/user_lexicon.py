USERS: dict[str: str] = {
    'greetings': 'Приветствую. 👋🏻\nЯ чат-бот компании «KanzOboz», я помогу вам '
                 'с трудоустройством и подбором вакансии, после чего с вами '
                 'менеджером.',
    'company': 'Основное направление деятельности нашей компании - '
               'производство и продажа канцелярских товаров по всей России. '
               'Мы занимаем большую долю рынка и осуществляем свою '
               'деятельность уже более 15 лет.\nГлавная ценность компании - '
               'наши сотрудники! Мы предоставляем комфортные условия труда, '
               'высокую заработную плату с ежедневными выплатами, гибкий '
               'график и специальные бонусы.',
    'main_manu': 'Вы в главном меню',
    'no_access': 'Сначала перейдите во вкладку О компании',
    'employment_info': 'Чтобы закрепить за вами место к дате встречи, '
                       'заполните небольшую вводную анкету.\nСогласны?',
    'refusal': 'Спасибо за обращение, можете посмотреть другие вакансии, '
               'возможно, они вам приглянутся больше.',
    'agreement': 'Так же сразу хочу предупредить Вас, что трудоутройство '
                 'возможно лишь через 7-10 дней, так как за это время мы '
                 'подготовим всё необходимое, есть ли у вас возможность '
                 'ждать столько?',
    'name_request': 'Отлично. Напишите как я могу к вам обращаться?',
    'city_request': 'В каком городе планируете трудоустройство?',
    'vacancies_request': 'Вакансия на которую планируете трудоустроиться:',
    'type_employment': 'Напишите желаемый вид трудоустройства:',
    'schedule': 'Остался последний момент, напишите желаемый график работы '
                '(например, Пн-Пт, 8.00-18.00):',
    'end_questionnaire': 'Все данные собраны, менеджер свяжется с вами '
                         'через 10-15 минут!',
    'jobs_in_city': 'Желаете посмотреть вакансии в вашем городе?',
    'city_input_2': 'Я могу подобрать вакансии, подходящие именно вам! '
                    'Укажите город вашего проживания:',
    'interesting_vacancies': 'Укажите интересующую вас вакансию:',
    'types_employment_1': 'Работа в данной должности возможна по следующим '
                          'видам занятости:\nПолная занятость - Полный '
                          'рабочий день (2/2, 3/3, 5/2);\nЧастичная '
                          'занятость - Сменами по 4-6 часов в день;'
                          '\nПодработка - от 2 часов в день.',
    'types_employment_2': 'Работа в данной должности возможна по следующим '
                          'видам занятости:\nПолная занятость - Полный '
                          'рабочий день (2/2, 5/2);\nПодработка - от 2 часов '
                          'в день.'
}

VACANCIES: dict[str: str] = {
    'driver': 'Водитель:\nВот кратко об условиях:\nМы предлагаем нашим '
              'сотрудникам:\n- автомобиль Lada Largus в исправном техническом '
              'состоянии(новая);\n- своевременную и стабильную оплату раз в '
              'неделю(возможно ежедневно на раннем этапе). 65 000 оклад + '
              'премии (которые зачастую больше зарплаты);\n- график работы: '
              '2/2 5/2. С 9:00 до 16:00 (раньше сделал - раньше освободился);'
              '\n-можно работать от 2х часов;\n- можно в виде подработки;\n'
              '- своевременное ТО автомобиля на СТО компании;\n- работу в '
              'дружном коллективе;\n- оформление как по ТК так и по желанию);'
              '\n- собственная парковка;\n- столовая на территории ( за счёт '
              'компании).\n\nОсновные обязанности:\n- осуществлять '
              'своевременную доставку канцелярии и офисной мебели;\n- '
              'обеспечивать сохранность груза при транспортировке;\n- ведение '
              'сопроводительной документации (обучаем, ничего сложного);\n'
              '- безаварийное вождение и соблюдение ПДД;\n- Материальную '
              'ценность нести не надо;\nТребования:\n- Опыт вождения;\n- '
              'Желание зарабатывать.',
    'sales_manager': 'Менеджер по продажам:\nОбязанности:\n-Обработка '
                     'входящих писем в чате;\n- Консультирование клиентов по '
                     'ассортименту продукции, качеству, свойствам, ценам;\n'
                     'Предоставление отчета о проделанной работе.\n- '
                     'Требования:\n- Активная жизненная позиция, '
                     'ответственность, самоорганизованность, желание '
                     'зарабатывать;\n- Коммуникабельность, умение вести '
                     'переговоры, креативность в плане общения и продаж;\n'
                     'базовые знания офисных программ.\nУсловия:\nГрафик '
                     'работы: 5/2 с 10:00 до 15:00 , 2/2 с 10:00 до 17:00;\n'
                     'Можно работать от 2-4 часов в день;\nОплата: оклад + '
                     'премиальные выплаты от завершенных сделок, в нашей '
                     'компании Ваш доход зависит от Вас! (От 85000 рублей) '
                     'оклад 45 000;\nОплата корпоративной мобильной связи;\n'
                     'Возможность карьерного роста до Руководителя отдела '
                     'продаж.',
    'salesman-cashier': 'Продавец-кассир:\nУсловия:\nМы предлагаем нашим '
                        'сотрудникам:\n- Своевременная выплата зарплаты '
                        'ежедневно или ежемесячно;\n- Заработная плата '
                        'продавца-кассира составляет от 55 000 (Выход-Смена: '
                        'оклад 2500 руб. + премия);\n-Скидки на продукцию '
                        'компании;\n- Карьерный рост;\n- Корпоративная '
                        'униформа;\n- Комфортные бытовые условия;\n- Обучение;'
                        '\n- График работы: 2/2; 3/3; 3/2; 4/3 (так же '
                        'рассматриваем подготовку от 3 х часов).\nОсновные '
                        'обязанности:\n- Производить выкладку товаров в '
                        'торговом зале;\n- Обслуживать/консультировать '
                        'покупателей в зале;\n- Проверять наличие и '
                        'соответствие ценников;\n- Работа с кассой(обучим).\n'
                        'Требования:\n- Желание работать и развиваться в '
                        'сфере обслуживания и продаж;\n- Доброжелательность, '
                        'внимательность, аккуратность;\n- Желание и умение '
                        'работать в команде;\n- Опыт работы не требуется, '
                        'всему обучаем.',
    'handyman': 'Работник склада (разнорабочий):\nМы предлагаем нашим '
                'сотрудникам:\n- Зарплата 45 000 оклад + премия по общим '
                'результатам компании;\n- График 5 *2, 2*2 обсуждается;\n'
                '- С 10/00 до 17:00 или с 10:00 до 15:00;\n- Можно работать '
                'от 2х часов (подработка);\n- Оплата ежедневно или '
                'ежемесячно.\nОсновные обязанности:\n- Приём товара;\n- '
                'Организация хранения товара;\n- Поддержание порядка на '
                'складе;\n- Подготовка товара к отгрузке и выдаче курьеру;\n'
                'Требования:\n- Быстрая и внимательная работа;\n- '
                'Дисциплинированность;\n- Желание зарабатывать.'
}

KEYBOARDS: dict[str: str] = {
    'vacancies': 'Актуальные Вакансии 🗂',
    'about_company': 'О компании ℹ️',
    'employment': 'Трудоустройство 🤝',
    'back_menu': 'Меню 📋',
    'yes': 'Да ✅',
    'no': 'Нет 🚫',
    'all_right': 'Всё верно',
    'correct': 'Исправить',
    'show_vacancies': 'Показать вакансии 🗂',
    'general': 'Общее',
    'middle': 'Среднее',
    'high': 'Высшее',
    'full_employment': 'Полная занятость',
    'part-time_employment': 'Частичная занятость',
    'part-time_job': 'Подработка',
    '2/2': '2/2',
    '3/3': '3/3',
    '5/2': '5/2',
    '3-4': '3-4',
    '5-6': '5-6',
    '1-2': '1-2',
    '2-4': '2-4',
    'driver': 'Водитель',
    'sales_manager': 'Менеждер по продажам'
}
