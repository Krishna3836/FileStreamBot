# (c) Jigarvarma2005 || Code-X-Mania || Tellybots

import os
import asyncio
from asyncio import TimeoutError
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.forcesub import handle_force_subscribe
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Code_X_Mania.add import add_user_to_database

#Recoded By @Tellybots

@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) & ~filters.edited, group=4)
async def private_receive_handler(c: Client, m: Message):
    await add_user_to_database(c, m)
    if Var.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(c, m)
      if fsub == 400:
        return
    try:        
        file_size = None
        if m.video:
            file_size = f"{humanbytes(m.video.file_size)}"
        elif m.document:
            file_size = f"{humanbytes(m.document.file_size)}"
        elif m.audio:
            file_size = f"{humanbytes(m.audio.file_size)}"
        elif m.photo:
            file_size=f"{humanbytes(m.photo.file_size)}"

        file_name = None
        if m.video:
            file_name = f"{m.video.file_name}"
        elif m.document:
            file_name = f"{m.document.file_name}"
        elif m.audio:
            file_name = f"{m.audio.file_name}"
        """
        elif m.photo:
            file_name=f"{m.photo.file_name}"
        """
            
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        
         
       
        
        
 
        msg_text = "Your Link Generated 📩\n\n🗄️ File Name : <code>{}</code>\n\n📇 File Size : <code>{}</code>\n\n🎥 Watch Online : <code>{}</code>"

        await log_msg.reply_text(text=f"**Requested By :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML", 
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎥 Watch Online", url=stream_link), #Stream Link
                                                InlineKeyboardButton('📩 Download Link', url=online_link)]]) #Download Link
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")

@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo) & ~filters.edited & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):  
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        online_link = Var.URL + 'download/' + str(log_msg.message_id) 
        await log_msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**Cʜᴀɴɴᴇʟ ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {stream_link}",
            quote=True,
            parse_mode="Markdown"
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🎥 Watch Online", url=stream_link)] 
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Got FloodWait Of {str(w.x)}s from {broadcast.chat.title}\n\n**Channel Id:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True, parse_mode="Markdown")
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel{e}**")
