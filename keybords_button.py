import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ТОКЕН
API_TOKEN = "6744538105:AAFWbWG--k5UYa4aWCLtVPLam8YVkpl18u8"

# Объявление бота
bot = Bot(API_TOKEN, parse_mode='HTML')
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    builder = ReplyKeyboardBuilder()

    # Список возможных команд
    button_text = ["Начать тренировку",
                   "Смотреть прогресс",
                   "Создать тренировку",
                   "Добавить упражнение"]
    for i in range(len(button_text)):
        builder.add(KeyboardButton(text=button_text[i]))

    # Сетка расположения кнопок клавиатуры (в данном случае 2х2)
    builder.adjust(2, 2)

    # Приветствие бота ИСПРАВИТЬ
    await message.answer(f"Hello <b>{message.from_user.first_name}</b>",
                         reply_markup=builder.as_markup(resize_keyboard=True))


async def main():
    # Удаление вебхуков (если до запуска бота ему приходили команды, то
    # после включения он не будет отвечать на каждую из этих команд)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
