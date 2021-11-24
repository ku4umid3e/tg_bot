import os
from pymongo import MongoClient
from emoji import emojize
from random import choice
from datetime import datetime

import settings


client = MongoClient(os.getenv("DB_link"))
db = client[os.getenv("DB_NAME")]


def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id,
            "emoji": emojize(choice(settings.USER_EMOJI), use_aliases=True),
        }
        db.users.insert_one(user)
    return user


def save_anketa(db, user_id, anketa_data):
    user = db.users.find_one({"user_id": user_id})
    anketa_data['created'] = datetime.now()
    if not 'anketa' in user:
        db.users.update_one(
            {'_id': user['_id']},
            {'$set':{'anketa': [anketa_data]}}
        )
