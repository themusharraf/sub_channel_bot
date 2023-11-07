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

# btnUrlChannel = types.InlineKeyboardButton(text="Obuna", url="https://t.me/daallnc")
# btnDoneSub = types.InlineKeyboardButton(text="Obuna check", callback_data="subchanneldone")
#
# checkSubMenu = types.InlineKeyboardMarkup(resize_keyboard=True)
# checkSubMenu.add(btnUrlChannel, btnDoneSub)


btnUrlChannel = InlineKeyboardButton(
    text="Obuna",
    url="https://t.me/daallnc"
)

btnDoneSub = InlineKeyboardButton(
    text="Obuna check",
    callback_data="subchanneldone"
)

# Create the InlineKeyboardMarkup and add the buttons
checkSubMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [btnUrlChannel, btnDoneSub]
    ]
)
# btnUrlChannel = InlineKeyboardBuilder()
# btnUrlChannel.add(InlineKeyboardButton(
#     text="Obuna",
#     url="https://t.me/daallnc")
# )
#
# btnDoneSub = InlineKeyboardBuilder()
# btnDoneSub.add(InlineKeyboardButton(
#     text="Obuna check",
#     callback_data="subchanneldone")
# )
#
# # Create the InlineKeyboardMarkup and add the buttons
# checkSubMenu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         btnUrlChannel.build(),
#         btnDoneSub.build()
#     ]
# )
#
#
