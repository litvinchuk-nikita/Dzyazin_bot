LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': f'Привет ! Я, ваш персональный тренер по фридайвингу, Дзязин Станислав. Научу вас красиво и глубоко нырять на одном вдохе.',
    '/help': f'Привет! Этот телеграмм-бот создан для записи на тренировки по фридайфингу. '
             f'Как он работает? Выбирайте дату и время тренировки, бронируйте занятие, после бронирования можно оплатить тенировку через бота. '
             f'Основные вопросы можно посмотреть в разделе "О нас", если не нашли ответ на ваш вопрос, зайдите в раздел "Часто задаваемые вопросы"\n\n'
             f'Доступные команды:\n'
             f'/start - Запустить бота/открыть меню\n'
             f'/help - Справка по работе бота',
    'info': f'<b>Как проводятся тренировки ?</b>\n'
            f'Тренировки проводятся только индивидуально, сначала немного теории, а затем 2-3 практических упражнения в воде (в воде находимся в среднем 45 минут).\n\n'
            f'<b>Cколько стоит тренировка ?</b>\n'
            f'Стоимость 1500₽/час.\n\n'
            f'<b>Что необходимо для треинирвки ?</b>\nОт вас только желание и гидрокостюм (гидрокостюм можно взять в аренду в клубе DEMERSUS за 500₽), а остальное снаряжение на время тренировки я вам предоставлю.\n\n'
            f'<b>Где проводятся тренировки ?</b>\nЖду вас на озере Янтарное (Синявинское озеро), Калининградская область, пгт. Янтарный, ул. Озерная 1, клуб DEMERSUS\n\n'
            f'<b>Когда проводятся тренировки ?</b>\nРегулярные тренировки проводятся с 15 мая по 15 сентября,'
            f' а с 15 сентября по 15 мая вам нужно заранее согласовать со мной время и дату,'
            f' так как в это время постоянно не нахожусь в клубе DEMERSUS\n\n'
            f'Ответы на другие интересующие вас вопросы вы найдете в разделе "Часто задаваемые вопросы".\n\n'
            f'Не нашли ответ на ваш вопрос или нужно согласовать время и дату тренировки ?\n\nСвяжитесь со мной:\ntelegram: @Dzyazin\nтелефон: +7-911-473-95-55\n\nС уважением, Станислав.',
    'sign_up': f'Выберите подходящую дату:',
    'date': f'Выберите подходящие время:',
    'video': 'https://youtu.be/aBWg2eqy5ZQ',
    'other': f'Не понимаю вас..\nДля ознакомления с возможностями бота введите команду /help',
    'pay': f'<b>Реквизиты для оплаты:</b>\n<b>Получатель</b> - Дзязин Станислав Васильевич;\n<b>Номер счета</b> - 40817810600008166761;\n'
           f'<b>Назначение платежа</b> - Перевод средств по договору № 5117723667 Дзязин Станислав Васильевич НДС не облагается\n'
           f'<b>БИК</b> - 044525974\n<b>Банк-получатель</b> - АО «Тинькофф Банк»\n<b>Корр. счет</b> - 30101810145250000974\n'
           f'<b>ИНН при необходимости</b> - 7710140679\n<b>КПП при необходимости</b> - 771301001\n\n<b>Перевод на карту:</b>\n'
           f'Тинькофф банк по номеру карты - 2200701108303287\n\nПосле осуществления перевода прошу вас отправить сриншот '
             f'с оплатой в ответ на это сообщение.\nДо встречи🙂',
    'menu_photo': 'https://img09.rl0.ru/afisha/e375x210p0x141f1347x758q85i/s2.afisha.ru/mediastorage/d8/68/44ab41ac943643259e649bff68d8.jpg'}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Запустить бота/открыть меню',
    '/help': 'Справка по работе бота'}

LEXICON_QUESTION: dict[str, str] = {
    '1': f'<b>Я боюсь воды, получиться у меня заниматься фридайвингом ?</b>\n\nДа, конечно, на тренировках я помогу вам, победить ваш страх!',
    '2': f'<b>Я не очень хорошо плаваю по поверхности воды, могу ли я научиться хорошо нырять ?</b>\n\nДа конечно, я научу вас красиво нырять от вас главное - это желание!',
    '3': f'<b>Сколько, занятий нужно, чтобы научится глубоко нырять ?</b>\n\nВ среднем, за 7-14 занятий с нуля, учу нырять на одном вдохе на глубину 20 метров.',
    '4': f'<b>На какую глубину, погружаемся на первом занятии ?</b>\n\nЕсли все нормально с компенсацией давления (продувкой), то до 6,5 метров.',
    '5': f'<b>Фридайвинг действительно положительно влияет на здоровье ?</b>\n\nДа, конечно положительно. Развиваются многие группы мышц. Растёт объем лёгких, улучшается эластичность лёгких.'
         f'Улучшается работа центральной нервной системы, сердца, сосудов и других внутренних органов. Легкие работают все лучше, и это отлично влияет на работу организма в целом '
         f'— ткани насыщаются кислородом, пропадает одышка, снижается отечность. Повышается стрессоустойчивость.',
    '6': f'<b>Могу ли я заниматься фридайвингом, после погружения с аквалангом (дайвинга) ?</b>\n\nНе совмещайте фридайвинг и дайвинг! Никакого фридайвинга 24 часа после погружений с аквалангом!',
    '7': f'<b>Кто может заниматься Фридайвингом?</b>\n\nФридайвинг не имеет возрастных ограничений и не требует специальной физической подготовки.'
         f' Фридайвером может стать каждый! Главное — квалифицированный инструктор, влюбленный в свое дело, который познакомит вас с этим увлекательным миром.',
    '8': f'<b>При каких заболеваниях противопоказаны занятия фридайвингом ?</b>\n\nЕсли у вас возник такой вопрос, советую обратиться к вашему лечащему врачу или терапевту.',
    '9': f'<b>Почему фридайверы ныряют с тросом. Зачем он нужен ?</b>\n\nТрос — это инструмент, который помогает сделать первые шаги, ровно как и учебная дорожка в бассейне.'
         f' Около него удобно ориентироваться, за него можно взяться, повисеть, научиться компенсировать давление и продувать уши. А потом уже можно нырять вдоль рифа, в открытом море без всяких канатов.',
    '10': f'<b>Каким навыкам в первую очередь вы обучаете ?</b>\n\nВ первую очередь это — расслабление, в том числе эмоциональное, и компенсация давления ушей.',
    '11': f'<b>Какую экипировку стоит приобрести новичку ?</b>\n\nДля начала стоит взять маску и гидрокостюм.',
    '12': f'<b>А какой нужен гидрокостюм ?</b>\n\nГидрокостюмов универсальных нет, они идут по нарастанию толщины. Есть тонкие (1-1,5 мм) для бассейнов и тёплых морей, где температура воды 27-30 градусов.'
          f' Где похолоднее, понадобятся костюмы толщиной в 3 мм. Для воды до 10 градусов — уже 5-7 мм. И 9 мм — для ледяной воды и более долгого нахождения в ней.',
    '13': f'<b>Как к вам добраться на занятие общественным транспортом из Калининграда ?</b>\n\nОт Калининграда можно доехать до Янтарного на 120 автобусе, остановка магазин "Азалия", а далее пешком примерно 1 километр.',
    '14': f'<b>Как к вам добраться на занятие общественным транспортом из Зеленоградска, Светлогорска, Пионерского ?</b>\n\nОт Зеленоградска, Светлогорска и Пионерского можно доехать до Янтарного на 587 автобусе, остановка "Янтарный комбинат", а далее пешком примерно 1 километр.',
    '15': f'<b>Тренируете в бассейне или в море ?</b>\n\nК сожалению, сейчас в ни бассейнах, ни в море не тренирую.',
    '16': f'<b>Как задержка дыхания влияет на сердце ?</b>\n\nЗамедляет сердечный ритм. Такая реакция является защитной и позволяет уменьшить потребление кислорода сердечной мышцей.',
    '17': f'<b>Сколько секунд задержка дыхания у здорового человека ?</b>\n\nВ норме задержка дыхания на вдохе составляет 55 — 60 секунд, но не менее 40 секунд.',
    '18': f'<b>Могу ли я занимаясь фридайвингом нанести вред здоровью ?</b>\n\nДа. Занимаясь фридайвингом самостоятельно, не имея необходимой подготовки, вы безусловно подвергаете своё здоровье и жизнь опасности.',
    '19': f'<b>Что такое компенсация давления (продувка) ?</b>\n\nНыряльщик зажимает нос рукой и постепенно несильно продувает через него воздух. Тем самым дайвер открывает евстахиевы трубы, что позволяет выровнять давление. Во время занятия я научу вас этому.',
    '20': f'<b>Хочу с вами понырять на затонувшие корабли на Балтийском море, это возможно ?</b>\n\nДа, конечно возможно, но сперва я дожжен провести с вами тестовую тренировку в озере Янтарное и определить ваш уровень подготовки.',
    '21': f'<b>Я пытаюсь самостоятельно тренировать задержку дыхания, это нормально ?</b>\n\nНе стоит заниматься самостоятельно без тренера или инструктора. Даже занимаясь со страхующем, не имеющего надлежащей подготовки, это очень опасно.',
    '22': f'<b>Есть ли у вас подарочные сертификаты ?</b>\n\nК сожалению пока что нет, но я думал об этом и скорее всего в ближайшее время сделаю.',
    '23': f'<b>Какая задержка дыхания нужна, чтобы нырнуть на глубину 20 метров ?</b>\n\nВ среднем у меня на занятиях ученики ныряют на глубину 20 метров от 40 секунд до 70 секунд. Но наиболее часто тренировочный нырок на глубину 20 метров занимает всего 1 минуту.',
    '24': f'<b>Вы делаете фото и видео съёмки под водой ?</b>\n\n Я пока не делаю фото и видео съёмку под водой (во время тренировки я смотрю за правильностью выполнения упражнения моими учениками и страхую их под водой и на поверхности воды). Безопасность важнее фото и видео.',
    '25': f'<b>Кто у вас делает фото и видео съёмки ?</b>\n\nПодводные съёмки моих занятий на задержке дыхания делает фридайвер — оператор - Павел Жорник',
    '26': f'<b>А какая у вас задержка дыхания ?</b>\n\nУ меня максимальная задержка дыхания в статике STA - 6 минут.',
    '27': f'<b>А сколько вы можете проплыть в длинну ?</b>\n\nМаксимально я проплывал в моноласте (DYN) 150 метров в длину в бассейне.',
    '28': f'<b>На какую глубину вы сами ныряете ?</b>\n\nЯ ныряю на глубину 55 метров в ласте и 42,5 метра без ласт.',
    '29': f'<b>Как давно вы занимаетесь фридайвингом ?</b>\n\nЯ занимаюсь фридайвингом с 2006 года, а инструктор по фридайвингу я с 2010 года.',
    '30': f'<b>С какой глубины вы можете спасти фридайвера ?</b>\n\nСпасение я регулярно тренирую с глубины 18,5 метров, а вот самая глубокая тренировка по спасению была с 40 метров.',
    '31': f'<b>Вы работаете с юридическими лицами ?</b>\n\nДа, конечно работаю. Я зарегистрирован как плательщик налога на профессиональный доход (самозанятый), так что безналичную оплату от юридического лица я принимаю.',
    '32': f'<b>Я давно не нырял, возможно восстановить навыки ? И если да, сколько это будет стоить ?</b>\n\nДа, конечно восстановления навыков возможно😉, стоимость как за обычное занятие 1500₽/час ! Я помогу вам восстановить и улучшить вашу спортивную форму!',
    '33': f'<b>Сколько стоимость прогулки на затонувший корабль DRACHE ?</b>\n\nВ среднем прогулка на катере к DRACHE обходится 15000₽, это если вы один ☝️, но за эту сумму вам возможно взять с собой ещё от 2-х до 4-х пассажиров, в зависимости от типа судна.',
    '34': f'<b>Вы можете обеспечить безопасность при погружениях на затонувший корабль DRACHE, если я буду нырять к кораблю на задержке дыхания ?</b>\n\n'
          f'Да, конечно это возможно, но это обговаривается индивидуально и после того как вы пройдёте со мной тестовое занятие на озере Янтарное и я увижу что вы готовы к таким погружениям😉',
    '35': f'<b>На какой глубине , корабль «DRACE» ?</b>\n\nDRACHE можно посмотреть и прикоснуться на глубинах от 20 до 28 метров.',
    '36': f'<b>Что самое сложное во фридайвинге ?</b>\n\nСамое сложное при нырянии в глубину — научиться компенсировать давление ушей, расслаблять грудную клетку и дыхательные мышцы. Если этого не сделать, может показаться, что воздух закончился — придёт ощущение пустых лёгких.'}


LEXICON_PHOTO: dict[str, str] = {
    '1': 'https://drive.google.com/file/d/1sKuHw9N1Qrecva_rq21TgPN-Zo2_0gUy/view?usp=drive_link',
    '2': 'https://4.downloader.disk.yandex.ru/preview/534ecbe6e6b20dec931925d19b4be2a2e25d4a9217c3b0150d8e23704bf1c99b/inf/qp2Q5ao1B7lONtQ5jQGMUMBAA3j6W6_fLgP8Ffsz85sqIt8tHkitpIqoWdtCo_0T7REaxM7AOdJxNyJjdQpOXQ%3D%3D?uid=1055291902&filename=2023-09-25%2012.44.08.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '3': 'https://3.downloader.disk.yandex.ru/preview/10aafd8f5e56b42f4abc5e01da86cedac3058d38302ab8122ca15558d02b578d/inf/sTHj7JiRuJpQ90vHqGqlzayhx4kBJ-thr-IMzn8BSc429FDggdxN_rafZ3Oetcyq09LMDx6vAsrGADSrAILPnQ%3D%3D?uid=1055291902&filename=2023-09-25%2012.44.17.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '4': 'https://2.downloader.disk.yandex.ru/preview/473533353e45c1236e8ad6a7f7ae67510c7d399a441c765669c8a43d8d987037/inf/wjJ-GRdOrBTNsMQTvMPBIgwDVDF4SPCuEcPjIpDCQIRnyB4yoscUQCVNZWalN7gr0wr5Y6Ff22-9D8qO0dWySQ%3D%3D?uid=1055291902&filename=2023-09-25%2012.44.33.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '5': 'https://2.downloader.disk.yandex.ru/preview/78984bb87c5bfa1a240b355080d9321ff0964de918f6072fd74f37ef13e946ea/inf/3Yw_zOfycU6At4MoO1xUU8BAA3j6W6_fLgP8Ffsz85udzx26nnhBLGdbHPsLfy_C84sOq7ccgTlJiz-N-7acdQ%3D%3D?uid=1055291902&filename=2023-09-25%2012.44.44.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '6': 'https://2.downloader.disk.yandex.ru/preview/862da3dd6bbd99a538fd7d6c3a1e3aa68855ac162d46bb6ea9a80a132dca1952/inf/n469-OfkSiKM2ECDRe-lhgwDVDF4SPCuEcPjIpDCQISRRwKQz3vHUkXUJmwTrNqUAd8daU2tADzpmqIvGz-a1g%3D%3D?uid=1055291902&filename=2023-09-25%2012.45.45.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '7': 'https://2.downloader.disk.yandex.ru/preview/75b252a6bb05e3092b3dc00d58cf690a9a2c773c81f98d05941df38e5253f7f7/inf/nKcxemveOWx3sIKClAmFOIE3TJvAX6hD6yu1ZGJQI9aTay2tk-iyTxRisr5rmbRQ2grjmpoJQukCTrMKqfh0YA%3D%3D?uid=1055291902&filename=2023-09-25%2012.45.51.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '8': 'https://2.downloader.disk.yandex.ru/preview/5856da692825f056e0031901783d8a56a37950313ba03eeeab266569d0822603/inf/MXprGNuiFzEyge0onxerWn09_7mGXzIWgtEGJYT4-YoILe0qQG6qlVv0-Af-qr7aqLv3AnXquQqY6YrVjfrvhw%3D%3D?uid=1055291902&filename=2023-09-25%2012.45.57.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566',
    '9': 'https://4.downloader.disk.yandex.ru/preview/92d6e83571728acc48a71bd57c5159b2bca987c2bdb63e36d3d81458097a3bfa/inf/5pjhkkTDanwPDahtE1TauOW-XDPaa4T5lLh1ByRGUJnt6-PIFTjNxinGvapeRGBkUKe6vs3c_kX0SONxhhrnIg%3D%3D?uid=1055291902&filename=2023-09-25%2012.46.06.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=1055291902&tknv=v2&size=2880x1566'}