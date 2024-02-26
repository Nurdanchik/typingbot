from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.exceptions import TelegramBadRequest


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Настроить игру'),
            KeyboardButton(text='Наши ссылки'),
        ],
        [
            KeyboardButton(text='Правила игры'),
        ],
        ],resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие в меню',
    selective=True,
)


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Instahram', url='https://instagram.com/nnyshanovv'),
            InlineKeyboardButton(text='GitHub', url='https://github.com/Nurdanchik/'),
        ]
    ]
)

languages_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Русский'),
            KeyboardButton(text='English'),
        ],
        ]
)

action_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Слово'),
            KeyboardButton(text='Буква'),
        ],
        ]
)