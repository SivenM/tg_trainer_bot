import json
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

with open('data_file.json', 'r', encoding='utf-8') as data_f:
    data_f = json.load(data_f)

class Menu:
    def __init__(self):
        self.start_txt = data_f["start_train"]
        self.creator_txt = data_f["creator"]
        self.progress_txt = data_f["watch_progress"]

    # Главное меню - функция отвечат за создание пользовательской клавиатуры
    def keybord_menu(self):
        builder = ReplyKeyboardBuilder()

        builder.add(KeyboardButton(text=self.start_txt))
        builder.add(KeyboardButton(text=self.creator_txt))
        builder.add(KeyboardButton(text=self.progress_txt))

        # Сетка расположения кнопок клавиатуры (в данном случае 2х2)
        builder.adjust(1, 2)
        return builder.as_markup(resize_keyboard=True)
        # return builder.as_markup(resize_keyboard=True, one_type_keybord=True)


class Creator:
    def __init__(self):
        self.add_txt = data_f["add_train"]
        self.edit_txt = data_f["edit_train"]
        self.delete_txt = data_f["delete_train"]

        self.plus_txt = data_f["plus"]
        self.minus_txt = data_f["minus"]
        self.ready_txt = data_f["ready"]
        self.back_txt = data_f["back"]

    def keybord_creator(self):
        # Добавление команд в пользовательскую клавиатуру
        buttons = [
            [InlineKeyboardButton(text=self.add_txt, callback_data="creator_add")],
            [InlineKeyboardButton(text=self.edit_txt, callback_data="creator_edit")],
            [InlineKeyboardButton(text=self.delete_txt, callback_data="creator_delete")]
            ]

        builder = InlineKeyboardMarkup(inline_keyboard=buttons)
        return builder
    
    def keybord_add(self):
        buttons = [
            [InlineKeyboardButton(text=self.plus_txt, callback_data="add_plus"),
             InlineKeyboardButton(text=self.minus_txt, callback_data="add_minus"),
             InlineKeyboardButton(text=self.ready_txt, callback_data="add_ready"),
             InlineKeyboardButton(text=self.back_txt, callback_data="add_back")]
            ]

        builder = InlineKeyboardMarkup(inline_keyboard=buttons)
        return builder

