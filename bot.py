import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import TOKEN, PASSWORD, R_ADMIN, C_ADMIN
from aiogram.filters import CommandStart, Command

bot = Bot(token=TOKEN)
dp = Dispatcher()

admin_waiting = set()
admin = set()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Вітаємо на нашому РП сервеві в телеграмі!. Комванди бота:\n"
                         "/info - інформація про бота\n"
                         "/help - допомога по командам\n"
                         "/register - створити анкету країни"
                         )

@dp.message(Command(commands=["info"]))
async def cmd_info(message: Message):
    await message.answer("Цей бот є офіційним нашого РП сервера в телеграмі. Розробник - @n1kitinua. (якщо є баги то писати розробнику)\n"
                         "Команди бота можна подивитися по команді /commandList.\n"
                         "Щоб створити анкету країни, скористайтеся командою /register.")

@dp.message(Command(commands=["commandList"]))
async def cmd_commandList(message: Message):
    await message.answer("1. /start - Запуск бота\n"
                         "2. /info - Інформація про бота\n"
                         "3. /help - Допомога і тех. підтримка\n"
                         "4. /register - Створити анкету країни\n"
                         "5. /ads - Тарифи на рекламу")

@dp.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer("1. Створіть анкету по команді /register.\n"
                         "Тех. підтримка рп: @Teufelslied_1\n"
                         "Тех. підтримка бота: @n1kitinua")

@dp.message(Command(commands=["register"]))
async def cmd_register(message: Message):
    await message.answer("Щоб створити анкету, будь ласка, надішліть наступну інформацію:\n"
                         "1. Назва країни\n"
                         "2. Столиця\n"
                         "3. Тип країни\n"
                         "4. Идеология и государственное устройство\n"
                         "5. Голова країни (президент, король і інші)\n"
                         "6. Органи влади\n"
                         "7. Офіційні мови\n"
                         "8. Валюта\n"
                         "9. Демографія\n"
                         "10. Основні релігії\n"
                         "11. Географічне розположення\n"
                         "12. Економіка\n"
                         "13. Армія\n"
                         "14. Рівень дослідження\n"
                         "15. Культура\n"
                         "16. Політика\n"
                         "17. Історія (коротка, по бажанню)\n"
                         "18. Символіка (прапор обов'язково і герб по бажанню)\n")

@dp.message(Command(commands=["ads"]))
async def cmd_ads(message: Message):
    await message.answer("Якщо ви хочете розмістити рекламу в нашому боті, будь ласка, зв'яжіться з адміністратором @n1kitinua.\n"
                         "Вартість реклами:\n"
                         "1. Реклама в чаті - 20 грн.\n"
                         "2. Реклама в каналі - 15 грн.\n"
                         "3. Реклама в боті (при викликанні кожної функції буде реклама) - 50 грн.\n"
                         "Для узгодження напишіть адміністратору: @n1kitinua. Відповідь буде протягом 24 годин.")

@dp.message(Command(commands=[R_ADMIN]))
async def cmd_admin(message: Message):
    if message.from_user.id in admin:
        await message.answer("Ви вже адмін.")
        return
    else:
        admin_waiting.add(message.from_user.id)
        await message.answer("Введіть пін код адміна:")

@dp.message(Command(commands=[C_ADMIN]))
async def cmd_admin_info(message: Message):
    if message.from_user.id in admin:
        await message.answer("Команди для адміна:\n"
                             "/ban - забанити користувача\n"
                             "/unban - розбанити користувача\n"
                             "/mute - замутити користувача\n"
                             "/unmute - розмутити користувача")
    else:
        await message.answer("Ви не є адміном.")
        
@dp.message(Command(commands=["ban"]))
async def cmd_ban(message: Message):
    if message.from_user.id in admin:
        await message.answer("Введіть ID користувача, якого хочете забанити: (ще не працює)")
        # Логіка бану користувача тут
    else:
        await message.answer("Ви не є адміном.")

@dp.message(Command(commands=["unban"]))
async def cmd_unban(message: Message):
    if message.from_user.id in admin:
        await message.answer("Введіть ID користувача, якого хочете розбанити: (ще не працює)")
        # Логіка розбану користувача тут
    else:
        await message.answer("Ви не є адміном.")

@dp.message(Command(commands=["mute"]))
async def cmd_mute(message: Message):
    if message.from_user.id in admin:
        await message.answer("Введіть ID користувача, якого хочете замутити: (ще не працює)")
        # логіка муту
    else:
        await message.answer("Ви не є адміном")

@dp.message(Command(commands=["unmute"]))
async def cmd_unmute(message: Message):
    if message.from_user.id in admin:
        await message.answer("Введіть ID користувача, якого хочете розмутити: (ще не працює)")
        # логіка розмуту
    else:
        await message.answer("Ви не є адміном")

@dp.message()
async def check_pin(message: Message):
    if message.from_user.id in admin_waiting:
        if message.text.startswith("/"):
            await message.answer("Ви скасували введення пін коду. Введіть /iAdmin щоб спробувати ще раз.")
            admin_waiting.remove(message.from_user.id)
            return
        if message.text == PASSWORD:
            await message.answer("Вітаю, ти адмін!")
            admin_waiting.remove(message.from_user.id)
            admin.add(message.from_user.id)
        else:
            await message.answer("Неправильний пін код. Спробуйте ще раз або введіть /start для повернення.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")