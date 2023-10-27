import json
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

with open('data_file.json', 'r', encoding='utf-8') as data_f:
    data_f = json.load(data_f)


# Главное меню - функция отвечат за создание пользовательской клавиатуры
def keybord_menu():
    builder = ReplyKeyboardBuilder()
    # button_text - список возможных команд на начальном экране клавиатуры
    btn_txt = [data_f["start_train"],
                data_f["creator"],
                data_f["watch_progress"]]

    # Добавление команд в пользовательскую клавиатуру
    for i in range(len(btn_txt)):
        builder.add(KeyboardButton(text=btn_txt[i]))

    # Сетка расположения кнопок клавиатуры (в данном случае 2х2)
    builder.adjust(1, 2)
    return builder


# Меню редактора - отвечает за создание клавиатуры для редактирования
def keybord_creator():
    builder_creator = ReplyKeyboardBuilder()

    btn_txt_creator = [data_f["edit_train"],
                       data_f["add_train"],
                       data_f["delete_train"],
                       data_f["back"]]
    

    # Расположение кнопок
    builder_creator.row(KeyboardButton(text=btn_txt_creator[0]))
    builder_creator.row(KeyboardButton(text=btn_txt_creator[1]), KeyboardButton(text=btn_txt_creator[2]))
    builder_creator.row(KeyboardButton(text=btn_txt_creator[3]))

    return builder_creator