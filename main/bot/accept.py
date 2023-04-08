"""© @MrMKN.git"""

# pyro module 
from pyrogram import Client, filters
from pyrogram.enums import ParseMode, ChatType, ChatMemberStatus
from pyrogram.errors import FloodWait

from main import Bot
from main.config import Config, Txt
from main.database import db

import asyncio

@Bot.on_message(filters.command("run") & ( filters.channel | filters.group ))
async def _accept(bot: Bot, msg):
    chat_id = msg.chat.id
    chat_type = msg.chat.type
    
    if chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        if msg.from_user:
            user = msg.from_user.id 
            get_user = await bot.get_chat_member(
                chat_id=chat_id,
                user_id=user
            )
            if get_user.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:                
                _ex = await msg.reply(
                    text="you are not admin"
                )
                await asyncio.sleep(3)
                await _ex.delete(True)
                return

    _userSession = await db.get_client(None, int(chat_id))

    if _userSession is None:
        empty_string = await msg.reply(
            text="No Session String or connection in this chat. So please check bot help",
            parse_mode=ParseMode.DEFAULT,
            disable_web_page_preview=True
        )                
        await asyncio.sleep(3)
        await empty_string.delete(True)
        return

    try: 
        UserBot = Client(
            name=":memory:",
            session_string=_userSession,
            in_memory=True
        )        
    except Exception as e:
        Config.LOGGER.error(e)
        await msg.reply_text(e)
        return
    try:
        await UserBot.connect()
    except ConnectionError:
        await UserBot.disconnect()
        await UserBot.connect()

    try:
       while True: # create loop is better techniq 🙃
           try:
               await UserBot.approve_all_chat_join_requests(chat_id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await UserBot.approve_all_chat_join_requests(chat_id) 
           except Exception as e:
               Config.LOGGER.error(e)
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await UserBot.approve_all_chat_join_requests(chat_id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await UserBot.approve_all_chat_join_requests(chat_id) 
           except Exception as e:
               Config.LOGGER.error(e)

    snd = await bot.send_message(chat_id, "✅️ Finished")
    await asyncio.sleep(5)
    await msg.delete(True)
    await snd.delete(True)
    return await UserBot.disconnect()














                         
