# (c) @code-x-mania
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from Code_X_Mania.utils.broadcast_helper import send_msg
from Code_X_Mania.utils.database import Database
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
broadcast_ids = {}

@StreamBot.on_message(filters.command("users") & filters.private & ~filters.edited)
async def sts(c: Client, m: Message):
    user_id=m.from_user.id
    if user_id in Var.OWNER_ID:
        total_users = await db.total_users_count()
        await m.reply_text(text=f"Total Users in DB: {total_users}", parse_mode="Markdown", quote=True)
        
        

