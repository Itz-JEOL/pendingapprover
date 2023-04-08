# © @MrMKN.git

from pyrogram import filters 
from pyrogram.types import *

from main import Bot
from main.database import db, add_user
from main.config import Config 


@Bot.on_message(filters.command("start") & filters.private)
async def _start(b, m):
    user = m.from_user
  
    await add_user(user.id)

    await m.reply(
        text=f"""Hai {user.mention} 💞"""
    ) 
