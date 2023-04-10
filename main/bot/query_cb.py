""" © @MrMKN.git """

# part of pyrogram
from pyrogram.types import *


from main import Bot



@Bot.on_callback_query()
async def main_cb_(bot, cb):
    data = cb.data
    msg = cb.message
    user = cb.from_user

    if data == "close":
       try:
           await msg.continue_propagation()
           await msg.delete(True)
       except Exception as e:
           Config.LOGGER.error(e)

    elif data == "start":
       await msg.edit_text("""Hai {user.mention} 
Iam An Advanced Bot With Awesome Features
• I can Auto Approve Join Requests
• I can Approve Pending Old Join Requests
→ Click The Below Button To Setup Me"""
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("👤 SUPPORT", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📯 UPDATES", url="https://t.me/Beta_BoTZ")
            ],[            
            InlineKeyboardButton("⚙️SETTINGS", callback_data="settings"),
            InlineKeyboardButton("🧿 ABOUT", callback_data="about") 
        ]])
    ) 
   
    elif data == "settings":
       await msg.edit_text("")

    elif data == "about":
        me = await bot.get_me()
        mention = me.mention
       await msg.edit_text("""✯ MY NAME : {mention}
✯ CREATOR : <a href=https://t.me/JEOL_TG>𝙅𝙀𝙊𝙇</a>
✯ DEVELOPER : <a href=https://t.me/mr_MKN>𝙈𝙧.𝙈𝙆𝙉 𝙏𝙂</a>
✯ LIBRARY : : PYROGRAM
✯ LANGUAGE : PYTHON3
✯ DATABASE : MONGODB
✯ SERVER : HEROKU""")

    elif data == "addchat":
       await msg.edit_text("")

    else:
       await cb.answer("OkDa", show_alert=True)                                                 
