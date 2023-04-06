"""© @MrMKN.git"""

from pyrogram import filters, types

from database import db



@Bot.on_message(filters.command("add") & filters.private)
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
        get_chat = await bot.get_chat(int(chat.text))
    except:
        await chat.reply("wrong chat id. Process Cancelled")
        return await chat.continue_propagation()

    if await db.get_chat(int(chat.text)):
        return await chat.reply("your channel is already added")

    await db.add_chat(int(chat.text))
    await chat.continue_propagation()























































                                                                                                                                                                                      
