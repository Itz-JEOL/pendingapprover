import motor.motor_asyncio
from main.config import Config


class Database:
    
    def __init__(self):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(Config.DB_URL)
        self.db = self._client[Config.DB_NAME]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,                       
            chat=None,
            session=None        
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
  
    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})
    
    async def add_chat(self, id, chat):
        await self.col.update_one({'id': int(id)}, {'$set': {'chat': int(chat)}})
 
    async def get_chat(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get("chat", None)
       
    async def del_chat(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'chat': None}})
        await self.col.update_one({'id': int(id)}, {'$set': {'session': None}})

    async def set_client(self, id, session):
        await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})

    async def get_client(self, id, chat):
        return await self.col.find_one({'id': int(id), 'chat': int(chat)} if id else {'chat': int(chat)})['session']                             
        


db = Database()


