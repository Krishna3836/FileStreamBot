# (c) @AbirHasan2005

import os
import time
import string
import random
import asyncio
import aiofiles
import datetime

from Code_X_Mania.utils.database import Database
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
broadcast_ids = {}





@StreamBot.on_message(filters.command("broadcast") & filters.private & ~filters.edited)
async def broadcast_(c, m):
    if user_id in Var.OWNER_ID:
       user_id = await db.get_all_users()
       broadcast_msg = message.reply_to_message
       txt = await message.reply(text = 'Staring....')        
       
       success = 0
       deleted = 0
       blocked = 0     
       await txt.edit(text = 'Broadcasting message, Please wait', reply_markup = None)   
       for user_id in user_ids:
          try:
            broadcast_msg = await broadcast_msg.copy(
            chat_id =user_id ,
            reply_to_message_id = broadcast_msg.message_id
            )
            success += 1
            time.sleep(3)
          except FloodWait as e:
            await asyncio.sleep(e.x)
            success += 1
          except UserIsBlocked:
            blocked += 1
          except InputUserDeactivated:
            deleted += 1                       
       text = f"""<b>Broadcast Completed</b>    
Total users: {str(len(user_ids))}
Deleted accounts: {str(deleted)} """
       await message.reply(text=text)
       await message.delete()


