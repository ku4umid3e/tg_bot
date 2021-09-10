import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings


logging.basicConfig(filename='bot.log', level=logging.INFO)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(update, context):
    # Информационный принт в терминал
    print("Вызван /start")
    # Ответное сообщение пользователю
    update.message.reply_text("Привет пользователь! Ты вызвал команду /start")

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.TOKEN, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Запись в журнал о начале работы бота.
    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


if __name__ == "__main__":
    main()