from datetime import datetime, date, timedelta
from copy import deepcopy
import requests
from config_data.config import Config, load_config
from aiogram import Router, F
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message, URLInputFile, InputMediaPhoto, ContentType
from database.database import user_dict_template, users_db, booking_db, time_list_template
from keyboards.pagination_kb import (create_pag_kb_question, create_pag_kb_photo)
from keyboards.other_kb import (create_menu_kb, create_info_kb, create_date_kb,
                                create_time_kb, create_confirmation_kb, create_pay_kb)
from lexicon.lexicon import LEXICON, LEXICON_QUESTION, LEXICON_PHOTO

router: Router = Router()


# загружаем конфиг в переменную config
config: Config = load_config()


# этот хэндлер будет срабатывать на команду "/start" -
# и отправлять ему стартовое меню
@router.message(CommandStart())
async def process_start_cammand(message: Message):
    if message.from_user.id not in users_db:
        users_db[int(message.from_user.id)] = deepcopy(
            user_dict_template)
        print(users_db)
    text = LEXICON['/start']
    photo = URLInputFile(url=LEXICON['menu_photo'])
    video = LEXICON['video']
    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_menu_kb(video))


# этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Вернуться в меню"
# во время взаимодействия пользователя с один из каталогов с товарами
@router.callback_query(Text(text='backword_menu'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON['/start']
    photo = URLInputFile(url=LEXICON['menu_photo'])
    video = LEXICON['video']
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=create_menu_kb(video))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "О нас"
# во время взаимодействия пользователя с меню
@router.callback_query(Text(text='info'))
async def process_info_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['info'],
        parse_mode='HTML',
        reply_markup=create_info_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Записаться на тренировку"
# во время взаимодействия пользователя с меню
@router.callback_query(Text(text='sign_up'))
async def process_sign_up_press(callback: CallbackQuery):
    date_list = []
    for i in range(7):
        now = date.today()
        date_1 = now + timedelta(days=i)
        date_1 = datetime.strftime(date_1, '%d.%m.%Y')
        date_list.append(date_1)
    date_1, date_2, date_3, date_4, date_5, date_6, date_7 = date_list[0], date_list[1], date_list[2], date_list[3], date_list[4], date_list[5], date_list[6]
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['sign_up'],
        reply_markup=create_date_kb(date_1, date_2, date_3, date_4, date_5, date_6, date_7))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки с датой
# во время выбора пользователя даты записи на тренировку
@router.callback_query(Text(text=['date_0', 'date_1', 'date_2', 'date_3', 'date_4', 'date_5', 'date_6']))
async def process_date_press(callback: CallbackQuery):
    time_list = deepcopy(time_list_template)
    date = callback.message.reply_markup.inline_keyboard[int(callback.data.split("_")[1])][0].text
    if date in booking_db:
        for i in range(5):
            if time_list[i] in booking_db[date]:
                time_list[i] = 'Уже забранировано🤷🏼‍♂'
    time_0, time_1, time_2, time_3, time_4 = time_list[0], time_list[1], time_list[2], time_list[3], time_list[4]
    await callback.message.delete()
    await callback.message.answer(
        text=f'Выбранная дата: {date} \n{LEXICON["date"]}',
        reply_markup=create_time_kb(time_0, time_1, time_2, time_3, time_4))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Назад"
# во время взаимодействия пользователя с выбором времени тренировки
@router.callback_query(Text(text='backword_date'))
async def process_backward_press(callback: CallbackQuery):
    date_list = []
    for i in range(7):
        now = date.today()
        date_1 = now + timedelta(days=i)
        date_1 = datetime.strftime(date_1, '%d.%m.%Y')
        date_list.append(date_1)
    date_1, date_2, date_3, date_4, date_5, date_6, date_7 = date_list[0], date_list[1], date_list[2], date_list[3], date_list[4], date_list[5], date_list[6]
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['sign_up'],
        reply_markup=create_date_kb(date_1, date_2, date_3, date_4, date_5, date_6, date_7))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки с временем
# во время выбора пользователя времени записи на тренировку
@router.callback_query(Text(text=['time_0', 'time_1', 'time_2', 'time_3', 'time_4']))
async def process_date_press(callback: CallbackQuery):
    date = callback.message.text.split(" ")[2]
    time = callback.message.reply_markup.inline_keyboard[int(callback.data.split("_")[1])][0].text
    if time == 'Уже забранировано🤷🏼‍♂':
        await callback.message.answer(
            text='Данное время уже занято, выберите другое.')
    else:
        await callback.message.delete()
        await callback.message.answer(
            text=f'Выбранная дата и время:\n {date} {time}',
            reply_markup=create_confirmation_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Назад"
# во время взаимодействия пользователя с подтверждением записи
@router.callback_query(Text(text='backword_time'))
async def process_backward_press(callback: CallbackQuery):
    time_list = deepcopy(time_list_template)
    date = callback.message.text.split(" ")[4]
    if date in booking_db:
        for i in range(5):
            if time_list[i] in booking_db[date]:
                time_list[i] = 'Уже забранировано🤷🏼‍♂'
    time_0, time_1, time_2, time_3, time_4 = time_list[0], time_list[1], time_list[2], time_list[3], time_list[4]
    await callback.message.delete()
    await callback.message.answer(
        text=f'Выбранная дата: {date} \n{LEXICON["date"]}',
        reply_markup=create_time_kb(time_0, time_1, time_2, time_3, time_4))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# подтверждения выбранного времени
@router.callback_query(Text(text='confirmation'))
async def process_confirmation_press(callback: CallbackQuery):
    date = callback.message.text.split(" ")[4]
    time = callback.message.text.split(" ")[5]
    if date not in booking_db:
        booking_db[date] = []
        booking_db[date].append(time)
    else:
        booking_db[date].append(time)
    await callback.message.delete()
    await callback.message.answer(
        text=f'Вы забронировали занятие по фридайвингу {date} в {time}.')
    params: dict[str, str] = {
        'chat_id': f'{config.tg_bot.admin_ids[1]}',
        'text': f'{callback.from_user.full_name} забронировал(а) '
        f'занятие по фридайвингу - {date} в {time}.\n'
        f'tg: @{callback.from_user.username}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)
    params: dict[str, str] = {
        'chat_id': f'{config.tg_bot.admin_ids[0]}',
        'text': f'{callback.from_user.full_name} забронировал(а) '
        f'занятие по фридайвингу - {date} в {time}.\n'
        f'tg: {callback.from_user.url}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)
    await callback.message.answer(
        text='Удобно ли вам будет оплатить занятие через нашего бота ?',
        reply_markup=create_pay_kb())


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Да"
# во время взаимодействия пользователя с предложением об оплате занятия
@router.callback_query(Text(text='yes'))
async def process_info_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=LEXICON['pay'],
        parse_mode='HTML')


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Нет"
# во время взаимодействия пользователя с предложением об оплате занятия
@router.callback_query(Text(text='no'))
async def process_info_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=f'В таком случае будет возможен перевод на карту или оплата наличными перед началом занятия.\nДо встречи🙂')


# этот хэндлер будет срабатывать отправку пользователем
# скрина об оплате
@router.message(F.content_type == ContentType.PHOTO)
async def process_page_sending(message: Message):
    params: dict[str, str] = {
        'chat_id': f'{config.tg_bot.admin_ids[1]}',
        'text': f'{message.from_user.full_name} оплатил(а) '
        f'занятие по фридайвингу.\ntg: @{message.from_user.username}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)
    await message.send_copy(chat_id=f'{config.tg_bot.admin_ids[1]}')
    params: dict[str, str] = {
        'chat_id': f'{config.tg_bot.admin_ids[0]}',
        'text': f'{message.from_user.full_name} оплатил(а) '
        f'занятие по фридайвингу.\ntg: @{message.from_user.username}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)
    await message.send_copy(chat_id=f'{config.tg_bot.admin_ids[0]}')


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Часто задаваемые вопросы"
# во время взаимодействия пользователя с меню
@router.callback_query(Text(text='question'))
async def process_question_press(callback: CallbackQuery):
    text = LEXICON_QUESTION[str(users_db[callback.from_user.id]['qu'])]
    pag = f'{str(users_db[callback.from_user.id]["qu"])}/{len(LEXICON_QUESTION)}'
    await callback.message.delete()
    await callback.message.answer(
        text=text,
        parse_mode='HTML',
        reply_markup=create_pag_kb_question(pag=pag))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком часто задаваемых вопросов
@router.callback_query(Text(text='forward'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['qu'] < len(LEXICON_QUESTION):
        users_db[callback.from_user.id]['qu'] += 1
    elif users_db[callback.from_user.id]['qu'] == len(LEXICON_QUESTION):
        users_db[callback.from_user.id]['qu'] = 1
    text = LEXICON_QUESTION[str(users_db[callback.from_user.id]['qu'])]
    pag = f'{str(users_db[callback.from_user.id]["qu"])}/{len(LEXICON_QUESTION)}'
    await callback.message.edit_text(
        text=text,
        parse_mode='HTML',
        reply_markup=create_pag_kb_question(pag=pag))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком часто задаваемых вопросов
@router.callback_query(Text(text='backward'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['qu'] > 1:
        users_db[callback.from_user.id]['qu'] -= 1
    elif users_db[callback.from_user.id]['qu'] == 1:
        users_db[callback.from_user.id]['qu'] = len(LEXICON_QUESTION)
    text = LEXICON_QUESTION[str(users_db[callback.from_user.id]['qu'])]
    pag = f'{str(users_db[callback.from_user.id]["qu"])}/{len(LEXICON_QUESTION)}'
    await callback.message.edit_text(
        text=text,
        parse_mode='HTML',
        reply_markup=create_pag_kb_question(pag=pag))


# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Фото с тренировки"
# # во время взаимодействия пользователя с меню
# @router.callback_query(Text(text='photo'))
# async def process_question_press(callback: CallbackQuery):
#     photo = URLInputFile(url=LEXICON_PHOTO[str(users_db[callback.from_user.id]['ph'])])
#     pag = f'{str(users_db[callback.from_user.id]["ph"])}/{len(LEXICON_PHOTO)}'
#     await callback.message.delete()
#     await callback.message.answer_photo(
#         photo=photo,
#         reply_markup=create_pag_kb_photo(pag=pag))


# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# # во время взаимодействия пользователя со списком фотографий
# @router.callback_query(Text(text='forward_ph'))
# async def process_forward_press(callback: CallbackQuery):
#     if users_db[callback.from_user.id]['ph'] < len(LEXICON_PHOTO):
#         users_db[callback.from_user.id]['ph'] += 1
#     elif users_db[callback.from_user.id]['ph'] == len(LEXICON_QUESTION):
#         users_db[callback.from_user.id]['qu'] = 1
#     photo = URLInputFile(url=LEXICON_PHOTO[str(users_db[callback.from_user.id]['ph'])])
#     pag = f'{str(users_db[callback.from_user.id]["ph"])}/{len(LEXICON_PHOTO)}'
#     await callback.message.answer_photo(
#         photo=photo,
#         reply_markup=create_pag_kb_photo(pag=pag))


# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# # во время взаимодействия пользователя со списком фотографий
# @router.callback_query(Text(text='backward_ph'))
# async def process_backward_press(callback: CallbackQuery):
#     if users_db[callback.from_user.id]['ph'] > 1:
#         users_db[callback.from_user.id]['ph'] -= 1
#     elif users_db[callback.from_user.id]['ph'] == 1:
#         users_db[callback.from_user.id]['ph'] = len(LEXICON_PHOTO)
#     photo = URLInputFile(url=LEXICON_PHOTO[str(users_db[callback.from_user.id]['ph'])])
#     pag = f'{str(users_db[callback.from_user.id]["ph"])}/{len(LEXICON_PHOTO)}'
#     await callback.message.answer_photo(
#         photo=photo,
#         reply_markup=create_pag_kb_photo(pag=pag))
