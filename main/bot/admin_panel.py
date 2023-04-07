from pyrogram import filters
from main import Bot

import os, sys, asyncio
from main.config import Config 


@Bot.on_message(filters.command("stats") & filters.user(Config.ADMINS))
async def stats(b, m):
    await m.reply(
        text=f"ippo onnuilla")




@Bot.on_message(filters.command("update") & filters.user(Config.ADMINS))      
async def bot_up(b, m):
    await m.reply_text("Updating........")
    os.system("git pull")
    asyncio.sleep(1)
    os.execl(sys.executable, sys.executable, "-m", "main")
 

@Bot.on_message(filters.command("restart") & filters.user(Config.ADMINS))
async def restart(b, m):
    await m.reply("restating.........")
    os.execl(sys.executable, sys.executable, "-m", "main")
 
