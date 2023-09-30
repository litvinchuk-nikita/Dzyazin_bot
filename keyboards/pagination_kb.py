from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_pag_kb_question(pag) -> InlineKeyboardMarkup:
    forward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['forward'], callback_data='forward')
    backward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['backward'], callback_data='backward')
    pag_button: InlineKeyboardButton = InlineKeyboardButton(
        text=pag, callback_data='pag')
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(backward_button, pag_button, forward_button, menu_button)
    kb_builder.adjust(3, 1)
    return kb_builder.as_markup()


def create_pag_kb_photo(pag) -> InlineKeyboardMarkup:
    forward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['forward'], callback_data='forward_ph')
    backward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['backward'], callback_data='backward_ph')
    pag_button: InlineKeyboardButton = InlineKeyboardButton(
        text=pag, callback_data='pag')
    menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Вернуться в меню', callback_data='backword_menu')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(backward_button, pag_button, forward_button, menu_button)
    kb_builder.adjust(3, 1)
    return kb_builder.as_markup()


# def create_pag_kb_md(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_md')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_md')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_cd(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_cd')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_cd')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_ssr(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_ssr')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_ssr')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_msr(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_msr')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_msr')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_csr(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_csr')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_csr')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_ind(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_ind')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_ind')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_skin(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_skin')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_skin')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()


# def create_pag_kb_tin(pag, text_but) -> InlineKeyboardMarkup:
#     price_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=text_but, callback_data='price')
#     forward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['forward'], callback_data='forward_tin')
#     backward_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=LEXICON['backward'], callback_data='backward_tin')
#     pag_button: InlineKeyboardButton = InlineKeyboardButton(
#         text=pag, callback_data='pag')
#     menu_button: InlineKeyboardButton = InlineKeyboardButton(
#         text='Вернуться в меню', callback_data='backword_menu')
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     kb_builder.add(price_button, backward_button,
#                    pag_button, forward_button, menu_button)
#     kb_builder.adjust(1, 3, 1)
#     return kb_builder.as_markup()
