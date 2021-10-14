import datetime
import ephem

from db import db, get_or_create_user

def planet_in_constellation(update, context):
    
    print(update.message.text)
    
    user_text = update.message.text.split()[-1]

    print(user_text)

    body = getattr(ephem, user_text.title().strip())
    now = datetime.datetime.now()
    update.message.reply_text(ephem.constellation(body(now)))


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(update, context):
    # Информационный принт в терминал
    print("Вызван /start")
    # Сохраним данные пользовыателя в DB
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    # Ответное сообщение пользователю
    update.message.reply_text(
        "Привет пользователь! Это простой бот, который пока мало что умеет."
        )
