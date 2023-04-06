"""© @MrMKN.git"""

# pyro module 
from pyrogram import Client, filters
from pyrogram.enums import ParseMode, ChatType, ChatMemberStatus
from pyrogram.errors import FloodWait

from main import Bot
from config import Config, Txt
from database import db

import asyncio

@Bot.on_message(filters.command("run") & ( filters.channel | filters.group ))
async def _accept(bot: Bot, msg):
    chat_id = msg.chat.id
    chat_type = msg.chat.type
    chat_title = msg.chat.title
    
    if chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        if msg.from_user:
            user = msg.from_user.id 
            get_user = await client.get_chat_member(
                chat_id=chat_id,
                user_id=user
            )
            if get_user.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:                
                _ex = await msg.reply(
                    text=Txt.NON_ADMIN
                )
                await asyncio.sleep(3)
                await _ex.delete(True)
                return

    _userSession = await db.get_client(chat_id)

    if _userSession is None:
        empty_string = await msg.reply(
            text=Txt.NO_SESSION,
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
    else:
        await bot.send_message(chat_id, Txt.FINISHED.format(chat_title))
    
















                         
