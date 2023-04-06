"""© MrMKN.git"""

from pyrogram import Client
from main.config import Config
from pyropatch import listen 

class Bot(Client): 
    def __init__(self):
        super().__init__(
            name="multi-accepter",
            session_string=Config.BOT_SESSION,
            plugins=dict(root="main/bot"),      
            workers=500,
        )
     
    async def start(self):
        await super().start()                      
        me = await self.get_me()                     
        Config.LOGGER.info("bot started......")
        
    async def stop(self, *args):       
        await super().stop()
        Config.LOGGER.info("Bot stopped. Bye.")



