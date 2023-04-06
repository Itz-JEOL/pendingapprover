from pyrogram import errors
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from database import *

#os.system("pip install ffmpeg -y")


API_ID = ""
API_HASH = ""
TOKEN = ""

JEOL = Client("JPYRO", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


@JEOL.on_message(filters.private & filters.command("start"))
async def hello(client: JEOL, message: Message):
    await message.reply("Hey! It's Just a Cloner Bot example source Code")

##Copy from here 

@JEOL.on_message(filters.private & filters.command("add"))
async def clone(bot: JEOL, msg: Message):
    text = await msg.reply("Usage:\n\n /add session string")
    phone = msg.command[1]
    add_user(phone)
    print(all_users())
    
    try:
        m = await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client( ":memory:", API_ID, API_HASH, session_string=phone, in_memory=True, plugins={"root": "handlers"})
        await client.start()
        idle()
        user = await client.get_me()
        await m.edit(f"Your Client Has Been Successfully Started As @{user.username}! ✅\n\nThanks for Cloning.")
    except Exception as e:
        print(e)
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")


op = users.find()
for kk in op:
    nam = [kk['bot_token']]
    for usr in nam:
        try:
            print(usr)
            app = Client("cache",api_id=API_ID, api_hash=API_HASH, bot_token=usr ,in_memory=True, plugins={"root": "handlers"})
            app.start()
        except errors.bad_request_400.AccessTokenExpired as e:
            print(e)
            remove_user(usr)



JEOL.start()
idle()
