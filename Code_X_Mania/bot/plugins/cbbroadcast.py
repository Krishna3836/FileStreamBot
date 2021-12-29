
# (c) @AbirHasan2005

import shutil
import psutil
from pyrogram import filters
from pyrogram.types import (
    Message
)
from Code_X_Mania.vars import Var
from pyrogram import Client



@Client.on_message(filters.command("broadcast") & filters.user(Var.OWNER_ID) & filters.reply & ~filters.edited)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)
