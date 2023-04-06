import motor.motor_asyncio

DB_URL = "mongodb+srv://MONGOO:MONGOO@cluster0.0a5cpqh.mongodb.net/?retryWrites=true&w=majority"        
DB_NAME = "Itz-Jeol"

class Database:
    
    def __init__(self):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
        self.db = self._client[DB_NAME]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            _id=id,
            id=id,            
            session=None,
            chat=None,          
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

    async def set_client(self, id, session):
        await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})

    async def get_client(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('session', None)

    async def set_chat(self, id, chat):
        await self.col.update_one({'id': int(id)}, {'$set': {'chat': chat}})

    async def get_chat(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('chat', None)



db = Database()


