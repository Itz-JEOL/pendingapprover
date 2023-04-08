"""© @MrMKN.git"""

# part of pyro
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import *
from main import Bot
from main.database import db
from main.config import Config 
from main import Bot

@Bot.on_message(filters.command("add_chat") & filters.private)
async def _add_user(bot: Bot, msg: Message):
  
    user_id = msg.from_user.id
    already = await db.get_chat(user_id) 
    if already is not None:
        return await msg.reply_text(f"sorry you have already a connection of {already}")

    chat = await bot.ask_message(
        chat_id=user_id,
        text="please send your (channel / group) id",       
    )
    if not chat.text:
        await chat.reply("wrong chat id. Process Cancelled")
        return await chat.continue_propagation()
    elif not chat.text.startswith("-100"):
        await chat.reply("wrong chat id. Process Cancelled")
        return await chat.continue_propagation()
  
    try:
        chat_id = int(chat.text)
        try:
            m_st = await bot.get_chat_member(chat_id, user_id)
        except:
            await chat.reply_text("**I am Not admin in this chat**")
            return await chat.continue_propagation()
    
        if m_st.status == ChatMemberStatus.MEMBER:
            await msg.reply_text("**you're not admin in this chat**")
            return await chat.continue_propagation()

        get_chat = await bot.get_chat(chat_id)
        await db.add_chat(user_id, get_chat.id)
        await chat.reply_text("✅️ Your Channel Added")
        return await chat.continue_propagation()
                  
    except PeerIdInvalid:
        await chat.reply("wrong chat id. Process Cancelled")
        return await chat.continue_propagation()

    
    
@Bot.on_message(filters.command("add_user") & filters.private)
async def _user_client(b: Bot, m: Message):
    user_id = m.from_user.id 
    chat = await db.get_chat(user_id)
    if chat is None:
        return await m.reply("you don't have any chats. /add_chat to add your chat")

    _a_user = await db.get_client(int(user_id), int(chat))
    if _a_user is not None:
        return await m.reply("you have already a userBot")

    ask = await b.ask_message(user_id, "please send your user session")
  
    await db.add_client(user_id, ask.text)
    return await ask.reply("done ✅️")




















































                                                                                                                                                                                      
