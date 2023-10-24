import asyncio
import json
import keybords_button
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ТОКЕН
API_TOKEN = "6744538105:AAFWbWG--k5UYa4aWCLtVPLam8YVkpl18u8"

# Объявление бота
bot = Bot(API_TOKEN, parse_mode='HTML')
dp = Dispatcher()

# Инициализация данных в json файле
with open('data_file.json', 'r', encoding='utf-8') as data_f:
    data_f = json.load(data_f)

# Команда "start" активирует пользовательскую клавиатуру
@dp.message(Command("start"))
async def start(message: Message):
    builder = keybords_button.keybord_menu()
    await message.answer(data_f["hello_text"], reply_markup=builder.as_markup(resize_keyboard=True))


# Создание тренировки
@dp.message(Command(data_f["create_train"]))
async def create_train(message: Message):
    pass


async def main():
    print("start")
    
    # Удаление вебхуков (если до запуска бота ему приходили команды, то
    # после включения он не будет отвечать на каждую из этих команд)
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускает бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())