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

START_TEXT = """Hey {}\n
I am Telegram File Direct Link Generator as well as File Streamer Bot.\n
✪ Use Help Command to Know how to Use me.\n
✪ Made With 💕 By @Tellybots_4u"""

            
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
            caption ="""Hi !
I am Telegram File to Link Generator Bot with Channel support.
Send me any file and get a direct download link and streamable link.!""",
            parse_mode="html",
            reply_markup=START_BUTTONS)
	await bot.send_message(
		msg.chat.id,
		'Use below buttons to interact with me',
		reply_markup=buttonz
	)
