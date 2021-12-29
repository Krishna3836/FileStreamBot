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
            
        




# Start Message
@StreamBot.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		START_TEXT.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(START_BUTTONS)
	)
	await bot.send_message(
		msg.chat.id,
		'Use below buttons or Commands To Use Me',
		reply_markup=buttonz
			one_time_keyboard=True,
			resize_keyboard=True
	)
            
    

    

      
            

