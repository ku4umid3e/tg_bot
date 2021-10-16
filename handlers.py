import datetime
import emoji
import ephem
from random import choice
from emoji import emojize

from db import db, get_or_create_user
import settings
from utils import main_keyboard


def planet_in_constellation(update, context):
    user_text = update.message.text.split()[-1]
    body = getattr(ephem, user_text.title().strip())
    now = datetime.datetime.now()
    update.message.reply_text(ephem.constellation(body(now)))


def talk_to_me(update, context):
    user_text = update.message.text
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    update.message.reply_text(
            f"Здастуй, {user['name']} {user['emoji']}! Ты написал: {user_text}"
            )

def greet_user(update, context):
    # Информационный принт в терминал
    print("Вызван /start")
    # Сохраним данные пользовыателя в DB
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    # Ответное сообщение пользователю
    update.message.reply_text(
        f"Привет пользователь{user['emoji']}Это простой бот, который пока мало что умеет.",
        reply_markup=main_keyboard()
        )


def usewr_coordinates(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    coords = update.message.location
    update.message.replay_text(
            f"Ваши координаты {coords} {user['emoji']}!",
            reply_markup=main_keyboard()
            )
