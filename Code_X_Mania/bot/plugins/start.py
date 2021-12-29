# (c) Code-X-Mania 
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
import logging
logger = logging.getLogger(__name__)

from Code_X_Mania.utils.human_readable import humanbytes

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

            
            
            
        
            
         
@StreamBot.on_message(filters.regex("follow"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Here The Follow Links</b>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Follow Me", url=f"https://github.com/Tellybots")
                            ]
                        ]
                    ),
                    parse_mode="HTML",
                    disable_web_page_preview=True)


            
    

    

                            
            
         

@StreamBot.on_message((filters.command("start") | filters.regex('start')) & filters.private & ~filters.edited)
async def start(b, m):
        await StreamBot.send_photo(
            chat_id=m.chat.id,
            photo ="https://telegra.ph/file/6331817952aaadba88819.jpg",
            caption = START_TEXT.format(m.from_user.mention),
            parse_mode="html",
            reply_markup=buttonz)                                                                                                                                                                                                                                               
                return
        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"
            
        elif get_msg.photo:
            file_size=f"{get_msg.photo.file_size}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"
        elif get_msg.photo:
            file_name=f"{get_msg.photo.file_name}"

        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        
        online_link = Var.URL + 'download/' + str(log_msg.message_id) 
       

        msg_text = "Your Link Generated 📩\n\n🗄️ File Name : <code>{}</code>\n\n📇 File Size : <code>{}</code>\n\n📥 Download Link : <code>{}</code>\n\n🎥 Watch Online : <code>{}</code>"

        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎥 Watch Online", url=stream_link), #Stream Link
                                                InlineKeyboardButton('📩 Download Link', url=online_link)]]) #Download Link
        )


@StreamBot.on_message(filters.regex('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):

        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\nMʏ Nᴇᴡ Fʀɪᴇɴᴅ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started Your Bot !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir You Are Banned To Use Me. Contact The Developer",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://i.ibb.co/ys3Tgpk/mtzijuhd-0.png",
                Caption="**Join Our Update Channel Or Support Group To Use Me!**\n\nDue To Overload Only Channel Subscriber Can Use Me",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("♻️ Join My Update Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something Went Wrong. Contact The Developer.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""Send me any file or video i will give you streamable link and download link.\n
        I also support Channels, add me to you Channel and send any media files and see miracle✨ also send /list to know all commands""",
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ DEV", url="https://t.me/Tellybots_4u")],
                [InlineKeyboardButton("💥 FOLLOW", url="https://github.com/tellybots")]
            ]
        )
    )
