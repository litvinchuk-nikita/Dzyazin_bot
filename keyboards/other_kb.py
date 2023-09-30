from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_menu_kb(video) -> InlineKeyboardMarkup:
    info_button: InlineKeyboardButton = InlineKeyboardButton(
        text='О нас', callback_data='info')
    sign_up_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Записаться на тренировку', callback_data='sign_up')
    # payment_button: InlineKeyboardButton = InlineKeyboardButton(
    #     text='Оплата', callback_data='payment')
    video_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Видео с погружения', url=video)
    # foto_button: InlineKeyboardButton = InlineKeyboardButton(
    #     text='Фото с погружения', callback_data='photo')
    question_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Часто задаваемые вопросы', callback_data='question')
    # contacts_button: InlineKeyboardButton = InlineKeyboardButton(
    #     text='Контакты', callback_data='contacts')
    kb_builder_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_menu.add(info_button, sign_up_button, video_button, question_button)
    kb_builder_menu.adjust(1, 1, 1, 1)
    return kb_builder_menu.as_markup()


def create_info_kb() -> InlineKeyboardMarkup:
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(menu_button)
    return kb_builder.as_markup()


def create_pay_kb() -> InlineKeyboardMarkup:
    button_1: InlineKeyboardButton = InlineKeyboardButton(
        text='Да', callback_data='yes')
    button_2: InlineKeyboardButton = InlineKeyboardButton(
        text='Нет', callback_data='no')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(button_1, button_2)
    return kb_builder.as_markup()


def create_date_kb(date_0, date_1, date_2, date_3, date_4, date_5, date_6) -> InlineKeyboardMarkup:
    date_1_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_0, callback_data='date_0')
    date_2_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_1, callback_data='date_1')
    date_3_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_2, callback_data='date_2')
    date_4_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_3, callback_data='date_3')
    date_5_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_4, callback_data='date_4')
    date_6_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_5, callback_data='date_5')
    date_7_button: InlineKeyboardButton = InlineKeyboardButton(
        text=date_6, callback_data='date_6')
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(date_1_button, date_2_button, date_3_button, date_4_button,
                               date_5_button, date_6_button, date_7_button, menu_button)
    kb_builder.adjust(1, 1, 1, 1, 1, 1, 1, 1)
    return kb_builder.as_markup()


def create_time_kb(time_0, time_1, time_2, time_3, time_4) -> InlineKeyboardMarkup:
    time_1_button: InlineKeyboardButton = InlineKeyboardButton(
        text=time_0, callback_data='time_0')
    time_2_button: InlineKeyboardButton = InlineKeyboardButton(
        text=time_1, callback_data='time_1')
    time_3_button: InlineKeyboardButton = InlineKeyboardButton(
        text=time_2, callback_data='time_2')
    time_4_button: InlineKeyboardButton = InlineKeyboardButton(
        text=time_3, callback_data='time_3')
    time_5_button: InlineKeyboardButton = InlineKeyboardButton(
        text=time_4, callback_data='time_4')
    backword_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Назад', callback_data='backword_date')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(time_1_button, time_2_button, time_3_button, time_4_button, time_5_button, backword_button)
    kb_builder.adjust(1, 1, 1, 1, 1, 1)
    return kb_builder.as_markup()


def create_confirmation_kb() -> InlineKeyboardMarkup:
    backword_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Назад', callback_data='backword_time')
    confirm_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Подтвердить', callback_data='confirmation')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(confirm_button, backword_button)
    return kb_builder.as_markup()


# def create_mask_kb() -> InlineKeyboardMarkup:
#     mask_davines_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Маски Davines', callback_data='mask_d')
#     mask_drsorbi_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Маски Dr. Sorbie', callback_data='mask_sr')
#     kb_builder_mask: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder_mask.add(mask_davines_button, mask_drsorbi_button)
#     kb_builder_mask.adjust(1, 1)
#     return kb_builder_mask.as_markup()


# def create_shampoo_kb() -> InlineKeyboardMarkup:
#     shampoo_davines_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Шампуни Davines', callback_data='shampoo_d')
#     shampoo_drsorbi_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Шампуни Dr. Sorbie', callback_data='shampoo_sr')
#     kb_builder_shampoo: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder_shampoo.add(shampoo_davines_button, shampoo_drsorbi_button)
#     kb_builder_shampoo.adjust(1, 1)
#     return kb_builder_shampoo.as_markup()


# def create_conditioner_kb() -> InlineKeyboardMarkup:
#     conditioner_davines_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Кондиционеры Davines', callback_data='cond_d')
#     conditioner_drsorbi_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Кондиционеры Dr. Sorbie', callback_data='cond_sr')
#     kb_builder_conditioner: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder_conditioner.add(conditioner_davines_button, conditioner_drsorbi_button)
#     kb_builder_conditioner.adjust(1, 1)
#     return kb_builder_conditioner.as_markup()



# # def create_baskets_kb(*args: str) -> InlineKeyboardMarkup:
# #     # создаем объект клавиатуры
# #     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
# #     # наполняем клавиатуру кнопками-закладками в порядке возрастания
# #     for button in args:
# #         kb_builder.row(InlineKeyboardButton(
# #             text=f'{button}',
# #             callback_data=f'{button.split("-")[0].strip()}'))
# #     # добавляем в клавиатуру в конце две кнопки "Редактировать и "Отменить"
# #     kb_builder.row(InlineKeyboardButton(
# #         text='Редактировать',
# #         callback_data='edit_basket'),
# #         InlineKeyboardButton(
# #             text='Вернуться в меню',
# #             callback_data='backword_menu'),
# #         width=2)
# #     return kb_builder.as_markup()


# def create_basket_kb(total_sum) -> InlineKeyboardMarkup:
#     sum_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=f'Оформить заказ: {total_sum}₽', callback_data='sum')
#     edit_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Редактировать', callback_data='edit')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder_basket: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder_basket.add(sum_button, edit_button, menu_button)
#     kb_builder_basket.adjust(1, 2)
#     return kb_builder_basket.as_markup()


# def create_zero_basket_kb() -> InlineKeyboardMarkup:
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder_zero_basket: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder_zero_basket.add(menu_button)
#     return kb_builder_zero_basket.as_markup()


# def create_basket_kb_2(total_sum) -> InlineKeyboardMarkup:
#     sum_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=f'Оформить заказ: {total_sum}₽', callback_data='sum')
#     edit_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Очистить корзину', callback_data='clear')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder_basket: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder_basket.add(sum_button, edit_button, menu_button)
#     kb_builder_basket.adjust(1, 2)
#     return kb_builder_basket.as_markup()
