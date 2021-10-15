import datetime
import ephem
from random import choice
from emoji import emojize

from db import db, get_or_create_user
import settings
from utils import main_keyboard


def planet_in_constellation(update, context):
    
    print(update.message.text)
    
    user_text = update.message.text.split()[-1]

    print(user_text)

    body = getattr(ephem, user_text.title().strip())
    now = datetime.datetime.now()
    update.message.reply_text(ephem.constellation(body(now)))


def talk_to_me(update, context):
    user_text = update.message.text
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    update.message.reply_text(
            f"Здастуй, {username} {get_smile(context.user_data)}! Ты написал: {user_text}"
            )

def greet_user(update, context):
    # Информационный принт в терминал
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    # Сохраним данные пользовыателя в DB
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    # Ответное сообщение пользователю
    update.message.reply_text(
        f"Привет пользователь{get_smile(context.user_data)}! Это простой бот, который пока мало что умеет."
        )

def get_smile(user_data):
    # Выбор случайного эмодзи из набора.
    if 'emiji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def usewr_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.replay_text(
            f"Ваши координаты {coords} {context.user_data['emoji']}!",
            replay_markup=main_keyboard()
            )
