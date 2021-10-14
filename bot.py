import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import planet_in_constellation, talk_to_me, greet_user

TOKEN = os.getenv("KEY")


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(TOKEN, use_context=True)

    dp = mybot.dispatcher
    # модуль ephem принимает на вход название планеты на английском, например /planet Mars
    dp.add_handler(CommandHandler("planet", planet_in_constellation))
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

