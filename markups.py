from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = [
    [
        types.KeyboardButton(text="Profile"),
    ],
]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"
)

btnUrlChannel = InlineKeyboardButton(
    text="kanal 🔊",
    url="https://t.me/daallnc",
    resize_keyboard=True
)

btnDoneSub = InlineKeyboardButton(
    text="Obunani tek 🔐",
    callback_data="subchanneldone",
    resize_keyboard=True
)

# Create the InlineKeyboardMarkup and add the buttons
checkSubMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [btnUrlChannel, btnDoneSub]
    ]
)
