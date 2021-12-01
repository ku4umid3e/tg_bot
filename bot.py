import os
import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
        ConversationHandler)

from anketa import (anketa_start, anketa_name, anketa_rating,
        anketa_comment, anketa_skip, anketa_dontknow)
from handlers import planet_in_constellation, talk_to_me, greet_user

TOKEN = os.getenv("KEY")


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(TOKEN, use_context=True)
    
    anketa = ConversationHandler(
            entry_points=[
                MessageHandler(Filters.regex('^(Заполнить анкету)$'),
                anketa_start)
                ],
            states={
                "name": [MessageHandler(Filters.text, anketa_name)],
                "rating":[MessageHandler(Filters.regex('^(1|2|3|4|5)$'),
                    anketa_rating)],
                "comment": [
                    CommandHandler('skip', anketa_skip),
                    MessageHandler(Filters.text, anketa_comment)
                    ]
            },
            fallbacks=[MessageHandler(
                Filters.text | Filters.video | Filters.photo | Filters.document
                | Filters.location, anketa_dontknow
                )]
            )
    dp = mybot.dispatcher
    # модуль ephem принимает на вход название планеты на английском, например /planet Mars
    dp.add_handler(CommandHandler("planet", planet_in_constellation))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(anketa)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Запись в журнал о начале работы бота.
    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

    
if __name__ == "__main__":
    main()

