# (c) Code-X-Mania 
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
import logging
logger = logging.getLogger(__name__)

from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.add import add_user_to_database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Code_X_Mania.forcesub import handle_force_subscribe
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import ReplyKeyboardMarkup


buttonz=ReplyKeyboardMarkup(
            [
                ["start","help"],
                ["about","ping"],
                ["status"]        
            ],
            resize_keyboard=True
        )

START_TEXT = """
✮ Hey {} ✮\n
<code>I am Telegram File To Link Bot</code>\n
<code>Use Help Command to Know how to Use me</code>\n
✮ Made With 💕 By @DKBOTZ ✮"""

HELP_TEXT = """
✮ Send Me Any File or Media\n
✮ Provide You Instant Direct Download link\n
✮ Add me in Your Channel as Admin To Get Direct Download link button and online Stream Link Button\n
"""

ABOUT_TEXT = """
🤖 My Name : DK LINK BOT\n
🚦 Version : <a href='https://telegram.me/DKBOTZ'>2.0</a>\n
🗃️ Library : <a href='https://pyrogram.org'>Click Here</a>\n
👲 Developer : <a href='https://telegram.me/DKBOTZHELP'>TellyBots_4u</a>\n
📦 Last Updated : <a href='https://telegram.me/DKBOTZHEP'>[ 15-Jan-22 ] 10:00 PM</a>"""

TEXT = """Use Below Button Or Command to Use Me"""

             
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♻️ Update Channel', url='https://telegram.me/DKBOTZ'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/DK_BOTZ')
        ],[
        InlineKeyboardButton('♨️ Help', callback_data='help'),
        InlineKeyboardButton('🗑️ Close', callback_data='close')
        ]]
)
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('🗑️ Close', callback_data='close')
        ]]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('♨️ Help', callback_data='help'),
        InlineKeyboardButton('🗑️ Close', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()       


@StreamBot.on_message((filters.command("start") | filters.regex('start')) & filters.private & ~filters.edited)
async def start(b, m):    
    if Var.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(b, m)
      if fsub == 400:
        return
    await add_user_to_database(b, m)
    await StreamBot.send_photo(
            chat_id=m.chat.id,
            photo ="https://telegra.ph/file/487a81462d054413bb921.jpg",
            caption = START_TEXT.format(m.from_user.mention),
            parse_mode="html",
            reply_markup=START_BUTTONS)            
    

    

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


        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML", 
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎥 Watch Online", url=stream_link)]]) #STREAM Link
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)

