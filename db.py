import os
from pymongo import MongoClient
from pymongo.common import WAIT_QUEUE_TIMEOUT


client = MongoClient(os.getenv("DB_link"))
db = client.testdb


def get_or_create_user(db, effective_user, chat_id):
    user = db.user.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id 
        }
        db.users.insert_one(user)
    return user