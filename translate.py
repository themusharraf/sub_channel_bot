# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     conn = sqlite3.connect("user_info.db")
#
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS user(
# 	 	id INTEGER
# 	 	)""")
#     conn.commit()
#     userid = message.chat.id
#     cursor.execute(f"SELECT id FROM user WHERE id = {userid}")
#     data = cursor.fetchone()
#     if data is None:
#         user_id = [message.chat.id]
#
#     await bot.send_message(userid, f"""welcome back""", reply_markup= ** menu)