from flask_pymongo import PyMongo

mongo = PyMongo()

def get_user_collection():
    return mongo.db.users
