""© MrMKN.git"""

from pyrogram import Client
from main.config import Config


class Bot(Client): 
    def __init__(self):
        super().__init__(
            name="multi-accepter",
            session_string=Config.BOT_SESSION,          
            workers=100,
        )
     
    async def start(self):
        await super().start()                      
        me = await self.get_me()                     
        print("bot started......")
        
    async def stop(self, *args):       
        await super().stop()
        print("Bot stopped. Bye.")



