from pyrogram import Client


API_ID = "14417186"
API_HASH = "21731d919d79f78de24bdf1f6ccd6921"
TOKEN = "5989405319:AAEqwAGfViL0aNNykXvX0D-bPRnxQc968zQ"

class Bot(Client): 
    def __init__(self):
        super().__init__(
            name="multi-accepter",
            session_string=BOT_SESSION,
            plugins={"root": "main"},
            workers=100,
        )
     
    async def start(self):
        await super().start()                      
        me = await self.get_me()                     
        self.id = me.id
        self.username = me.username
        print("bot started......")
        
    async def stop(self, *args):       
        await super().stop()
        print("Bot stopped. Bye.")


Bot().run()







