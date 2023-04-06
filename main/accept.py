from pyrogram import Client, filters







async def accept(bot, msg):
    user_bot = await db.get_client(user_id)
    if user_bot is None:
        return await m.reply(text="Sorry Dude You Don't Have UserBot place add user session")                

