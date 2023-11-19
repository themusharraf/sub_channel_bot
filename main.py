import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from markups import keyboard, checkSubMenu
from root import settings
from aiogram.types import CallbackQuery
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.bots.bot_token)
dp = Dispatcher()
db = Database("preson.db")
not_sub_message = "kanalga obuna buling !"


def check_sup_channel(chat_member):
    print(chat_member.status)
    if chat_member.status != 'left':
        return True
    else:
        return False


@dp.message(Command("start"))
async def start(message: types.Message):
    if message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            if check_sup_channel(
                    chat_member=await bot.get_chat_member(chat_id=settings.bots.channel_id,
                                                          user_id=message.from_user.id)):
                await bot.send_message(message.from_user.id, "salom")  # reply_markup=keyboard
            else:
                await bot.send_message(message.from_user.id, not_sub_message, reply_markup=checkSubMenu)


@dp.message(Command("random"))
async def bot_message(message: types.Message):
    if message.chat.type == "private":
        if check_sup_channel(
                chat_member=await bot.get_chat_member(chat_id=settings.bots.channel_id, user_id=message.from_user.id)):

            await bot.send_message(message.from_user.id, f" sizng raqamingiz {random.randint(700, 800)} ",
                                   reply_markup=keyboard)  #

        else:
            await bot.send_message(message.from_user.id, "No check_sup_channel")
    else:
        await bot.send_message(message.from_user.id, not_sub_message, reply_markup=checkSubMenu)


@dp.message(Command("sendall"))
async def sendallll(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id == 5751237091:
            text = message.text[9:]
            users = db.get_user()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, f"uspeshni rasiilka {users[1]}")


async def main():
    await dp.start_polling(bot)


@dp.callback_query(lambda c: c.data == "subchanneldone")
async def subchanneldone(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)

    if check_sup_channel(
            chat_member=await bot.get_chat_member(chat_id=settings.bots.channel_id, user_id=call.from_user.id)):
        await bot.send_message(call.from_user.id, "salom")  # reply_markup=keyboard
    else:
        await bot.send_message(call.from_user.id, not_sub_message, reply_markup=checkSubMenu)
        text = "Kanalga obuna bo'lmagansiz ⚠️"
        show_alert = True
        await call.answer(text, show_alert=show_alert)


if __name__ == "__main__":
    asyncio.run(main())
