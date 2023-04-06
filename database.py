from pymongo import MongoClient

client = MongoClient("mongodb+srv://MONGOO:MONGOO@cluster0.0a5cpqh.mongodb.net/?retryWrites=true&w=majority")

users = client['main']['bots']


def already_db(user_id):
        user = users.find_one({"session_string" : str(user_id)})
        if not user:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"session_string": str(user_id)}) 

def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"session_string": str(user_id)})

def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs
