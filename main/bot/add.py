"""© @MrMKN.git"""

# part of pyro
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import *


from database import db



@Bot.on_message(filters.command("add_chat") & filters.private)
async def _add_user(bot: Bot, msg: types.Message):
  
    user_id = msg.from_user.id    
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
        m_st = bot.get_chat_member(chat_id, user_id)
        if m_st.status == ChatMemberStatus.MEMBER:
            return await msg.reply_text("**you're not admin in this chat**")
        b_st = bot.get_chat_member(chat_id, "me")
        if b_st.status == ChatMemberStatus.ADMINISTRATOR:
            get_chat = await bot.get_chat(chat_id)
            added = await db.add_chat(user_id, get_chat.id)
            if added:
                await chat.reply_text("✅️ Your Channel Added")
                return await chat.continue_propagation()
            else:             
                await chat.reply("your channel is already added")
                return await chat.continue_propagation() 
        else:
            await chat.reply_text("**I am Not admin in this chat**")
            return await chat.continue_propagation()       
    except PeerIdInvalid:
        await chat.reply("wrong chat id. Process Cancelled")
        return await chat.continue_propagation()

    
    
@Client.on_propagation(*args = True)
























































                                                                                                                                                                                      
