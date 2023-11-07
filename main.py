import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from markups import keyboard, checkSubMenu
from root import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.bots.bot_token)
dp = Dispatcher()

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
        if check_sup_channel(
                chat_member=await bot.get_chat_member(chat_id=settings.bots.channel_id, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "salom", reply_markup=keyboard)
        else:
            await bot.send_message(message.from_user.id, not_sub_message, reply_markup=checkSubMenu)


@dp.message()
async def bot_message(message: types.Message):
    if message.chat.type == "private":
        if check_sup_channel(
                chat_member=await bot.get_chat_member(chat_id=settings.bots.channel_id, user_id=message.from_user.id)):
            if message.text == "Profile":
                await bot.send_message(message.from_user.id, "my tg profil")
            else:
                await bot.send_message(message.from_user.id, "No check_sup_channel")
        else:
            await bot.send_message(message.from_user.id, not_sub_message, reply_markup=checkSubMenu)


async def main():
    await dp.start_polling(bot)


@dp.callback_query(text="subchanneldone")
async def subchanneldone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    if check_sup_channel(
            chat_member=await bot.get_chat_member(chat_id=settings.bots.channel_id, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "salom", reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, not_sub_message, reply_markup=checkSubMenu)

if __name__ == "__main__":
    asyncio.run(main())
