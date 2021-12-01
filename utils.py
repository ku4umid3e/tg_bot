from telegram import ReplyKeyboardMarkup
from telegram.keyboardbutton import KeyboardButton


def main_keyboard():
    return ReplyKeyboardMarkup([[
        "Заполнить анкету",
     KeyboardButton('Мои координаты', request_location=True),
     ]], resize_keyboard=True)
