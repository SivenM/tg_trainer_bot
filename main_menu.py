import asyncio
import json
import keybords_button
from db import Database
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ТОКЕН
API_TOKEN = "6744538105:AAFWbWG--k5UYa4aWCLtVPLam8YVkpl18u8"

# Объявление бота
bot = Bot(API_TOKEN, parse_mode='HTML')
dp = Dispatcher()

# Инициализация данных в json файле
with open('data_file.json', 'r', encoding='utf-8') as data_f:
    data_f = json.load(data_f)

# импорт базы данных
database_sql = Database(data_f["name_database"])


# Команда "start" активирует пользовательскую клавиатуру
@dp.message(Command("start"))
async def start(message: Message):

    ##### Создание БД и добавление новых пользователей в БД (id, username, first_name, last_name, premium)
    id = message.from_user.id
    username =  message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    is_premium = 1 if message.from_user.is_premium else 0
    print(id)
    print(username)
    print(first_name)
    print(last_name)
    print(is_premium)

    database_sql.create_trable()
    
    if message.chat.type == "private":
        if not database_sql.user_exists(id):
            database_sql.add_user(id, username, first_name, last_name, is_premium)
    #####

    builder = keybords_button.Menu().keybord_menu()
    await message.answer(data_f["hello_text"], reply_markup=builder)


# Кнопка редактора
@dp.message(F.text==data_f["creator"])
async def create_train(message: Message):
    print("creator")
    builder_creator = keybords_button.Creator().keybord_creator()
    await message.answer(data_f["creator_text"], reply_markup=builder_creator)


@dp.callback_query(F.data.startswith("creator_"))
async def callback_query_keybord(callback_query: CallbackQuery):
    action = callback_query.data.split("_")[1]
    if action == "add":
        print("Создать треню")
        builder_add = keybords_button.Creator().keybord_add()
        await callback_query.message.edit_text(text=data_f["add_text"], reply_markup=builder_add)
    elif action == "edit":
        print("Редактировать треню")
    elif action == "delete":
        print("Удалить треню")

@dp.callback_query(F.data.startswith("add_"))
async def callback_query_keybord(callback_query: CallbackQuery):
    action = callback_query.data.split("_")[1]
    if action == "back":
        print("Назад в Редактор")
        builder_add = keybords_button.Creator().keybord_creator()
        await callback_query.message.edit_text(text=data_f["creator_text"], reply_markup=builder_add)




async def main():
    print("start")
    
    # Удаление вебхуков (если до запуска бота ему приходили команды, то
    # после включения он не будет отвечать на каждую из этих команд)
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускает бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())