from aiogram import Bot, Dispatcher, executor, types
import asyncio

API_TOKEN = "7834664942:AAGa8iVWJ_fs1JRfDa5q99r5tQ0sSRFpP4k"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Welcome in 'New German World', this is official telegam bot!")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)