# © @MrMKN.git

from pyrogram import filters 
from pyrogram.types import *

from main import Bot
from main.database import db
from main.config import Config 


@Bot.on_message(filters.command("start") & filters.private)
async def _start(b, m):
    user = m.from_user
  
    await db.add_user(user.id)

    await m.reply(
        text=f"""Hai {user.mention} 💞""",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("👤 SUPPORT", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📯 UPDATES", url="https://t.me/Beta_BoTZ")
            ],[            
            InlineKeyboardButton("⚙️SETTINGS", callback_data="settings"),
            InlineKeyboardButton("🧿 ABOUT", callback_data="about") 
        ]])
    ) 
