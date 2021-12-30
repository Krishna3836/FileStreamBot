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
<b>Hey </b> <b>{}</b>\n
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

TEXT = """Use Below Button Or Command to Use Me"""

             
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
)
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
)        

    
@StreamBot.on_message((filters.command("start") | filters.regex('start')) & filters.private & ~filters.edited)
async def start(b, m):
    if Var.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(b, m)
      if fsub == 400:
        return
    await add_user_to_database(b, m)
    await StreamBot.send_photo(
            chat_id=m.chat.id,
            photo ="https://telegra.ph/file/0f0d8a7370ff48b48d664.jpg",
            caption = START_TEXT.format(m.from_user.mention),
            parse_mode="html",
            reply_markup=START_BUTTONS)
    #await m.reply_text(
            #text=TEXT,
            #parse_mode="HTML",
            #disable_web_page_preview=True,
            #reply_markup=buttonz
           #)
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

@StreamBot.on_message((filters.command("help") | filters.regex('help')) & filters.private & ~filters.edited)
async def help(bot, update):
    await add_user_to_database(bot, update)
    if Var.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )
  .
################## login command ##################

@Streambot.on_message(filters.command('login') & filters.incoming & filters.private)
async def password(c, m):
    if Config.BOT_PASSWORD:
        if m.from_user.id in Var.AUTH_USERS:
            return await m.reply_text(f"__Hey you are auth user of this bot so you don't want to login {DETECTIVE_LIGHT_SKIN_TONE}.__")

        is_logged = (await get_data(m.from_user.id)).is_logged
        if is_logged:
            return await m.reply_text(f"__You are already loggedin {VICTORY_HAND}.__", quote=True)

        if len(m.command) == 1:
            await m.reply_text('Send me the bot password in the format `/login password`')
        else:
            cmd, pwd = m.text.split(' ', 1)
            if pwd == Config.BOT_PASSWORD:
                await update_login(m.from_user.id, True)
                await m.reply_text(text=LOCKED_WITH_KEY, quote=True)
                await m.reply_text(f'Logged Sucessfully to the bot.\nEnjoy the bot now {FACE_SAVORING_FOOD}.', quote=True)
            else:
                await m.reply_sticker(sticker="CAACAgQAAxkBAAIlHWC8WTwz55v_w0laDRuSrwL2oWRTAALtDAACYLUpUtRT8sziJp59HwQ", quote=True)
                return await m.reply_text(f'Incorrect password', quote=True)
    else:
        await m.reply_text(f'**This bot was publicly available to all {SMILING_FACE_WITH_HEARTS}.**\nIf you are the owner of the bot to make bot private add bot password in Config Vars {LOCKED_WITH_KEY}.', quote=True)



@StreamBot.on_message((filters.command("about") | filters.regex('about')) & filters.private & ~filters.edited)
async def about(bot, update):
    await add_user_to_database(bot, update)
    """Processing Your Request"""

    if Var.BANNED_USERS:
        if m.from_user.id in Var.BANNED_USERS:
            return await m.reply_text(TEXT.BANNED_USER_TEXT, quote=True)

    if Var.BOT_PASSWORD:
        is_logged = (await get_data(m.from_user.id)).is_logged
        if not is_logged and m.from_user.id not in Var.AUTH_USERS:
            return await m.reply_text(TEXT.NOT_LOGGED_TEXT, quote=True)
    if Var.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    ) 
