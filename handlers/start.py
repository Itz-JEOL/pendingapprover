from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters
from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait


@Client.on_message(filters.private & filters.command("start"), [".", "/"])
async def start(client: Client, message: Message):
    await message.edit("Iam Alive \n\nPowered By @BETA_BOTZ \n\nSUBSCRIBE Youtube.com/@itzjeol")

    
@Client.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client: User, message: Message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq 🙃
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               print(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               print(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await asyncio.sleep(3)
    await msg.delete()    
