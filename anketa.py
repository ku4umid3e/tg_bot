from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from utils import main_keyboard

from db import db, get_or_create_user, save_anketa


def anketa_start(update, context):
    update.message.reply_text(
            "Как вас зовут? Напишите Имя и Фамилию",
            reply_markup=ReplyKeyboardRemove()
            )
    return "name"


def anketa_name(update, context):
        user_name = update.message.text
        if len(user_name.split()) < 2:
            update.message.reply_text("Пожалуйста, напишите Имя и Фамилию")
            return 'name'
        else:
            context.user_data['anketa'] = {'name':  user_name}
            reply_keyboard = [['1', '2', '3', '4', '5']]
            update.message.reply_text(
                    "Оцените бота по шкале от 1 до 5",
                    reply_markup=ReplyKeyboardMarkup(
                        reply_keyboard, one_time_keyboard=True, resize_keyboard=True
                        ))
            return 'rating'


def anketa_rating(update, context):
    context.user_data['anketa']['rating'] = int(update.message.text)

    update.message.reply_text(
            "Оствате комментарий в свободной форме или пропустите этот шагб введя /skip"
            )
    return "comment"


def anketa_comment(update, context):
    context.user_data['anketa']['comment'] = update.message.text
    user_text = anketa_format(context.user_data['anketa'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(),
            parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def anketa_skip(update, context):
    user_text =  anketa_format(context.user_data['anketa'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(),
            parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def anketa_format(anketa):
    user_text = f"""<b>Имя Фамилия:</b> {anketa['name']}
    <b>Оценка:</b> {anketa['rating']}"""
    if anketa.get('comment'):
        user_text += f"\n<b>Комментарий:</b> {anketa['comment']}"

    return user_text
   

def anketa_dontknow(update, context):
    update.message.reply_text("Не понимаю")
