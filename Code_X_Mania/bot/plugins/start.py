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


from pyrogram.types import ReplyKeyboardMarkup


buttonz=ReplyKeyboardMarkup(
            [
                ["start","help"],
                ["follow","ping"]
                        
            ],
            resize_keyboard=True
        )

START_TEXT = """
<b>Hey </b> {}\n
<b>I am Telegram File Direct Link Generator as well as File Streamer Bot. </b>\n
<b>✪ Use Help Command to Know how to Use me.</b>\n
<b><b>✪ Made With 💕 By </b>@Tellybots_4u</b>"""

HELP_TEXT = """
<b>✪ Send Me Any File or Media .</b>\n
<b>✪ I Will Provide You Instant Direct Download link and Online Streaming link.</b>\n
<b>✪ Add me in Your Channel as Admin To Get Direct Download link button and online Stream Link Button </b>\n
<b>✪ Streaming Link as well as Instant Link Generator With Fastest Speed</b>\n
"""

ABOUT_TEXT = """
<b>🤖 My Name : Telly File Stream Bot</b>\n
<b>🚦 Version : <a href='https://telegram.me/tellybots_4u'>2.0</a></b>\n
<b>💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a></b>\n
<b>🗃️ Library : <a href='https://pyrogram.org'>Click Here</a></b>\n
<b>👲 Developer : <a href='https://telegram.me/tellybots_4u'>TellyBots_4u</a></b>\n
<b>📦 Last Updated : <a href='https://telegram.me/tellybots_4u'>[ 15-Oct-21 ] 10:00 PM</a></b>"""

TEXT = """Use Below Button Or Command to use Me"""

            
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Help', callback_data='help'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]            
)            
        
 
@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private & ~filters.edited)
async def start(b, m):
        await StreamBot.send_photo(
            chat_id=m.chat.id,
            photo ="https://user-images.githubusercontent.com/88939380/137127129-a86fc939-2931-4c66-b6f6-b57711a9eab7.png",
            caption = START_TEXT,
            parse_mode="html",
            reply_markup=START_BUTTONS)
        await m.reply_text(
            text=TEXT,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=buttonz
              )
