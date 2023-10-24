import json
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

with open('data_file.json', 'r', encoding='utf-8') as data_f:
    data_f = json.load(data_f)


# функция отвечат за создание пользовательской клавиатуры
def keybord_menu():
    builder = ReplyKeyboardBuilder()

    # button_text - список возможных команд на начальном экране клавиатуры
    button_text = [data_f["start_train"],
                    data_f["watch_progress"],
                    data_f["create_train"],
                    data_f["add_exercise"]]

    # Добавление команд в пользовательскую клавиатуру
    for i in range(len(button_text)):
        builder.add(KeyboardButton(text=button_text[i]))

    # Сетка расположения кнопок клавиатуры (в данном случае 2х2)
    builder.adjust(2, 2)

    return builder
