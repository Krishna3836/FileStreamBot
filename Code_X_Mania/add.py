# (c) @AbirHasan2005


from Code_X_Mania.vars import Var
from .database import db
from Code_X_Mania.bot import StreamBot
from pyrogram.types import Message


async def add_user_to_database(bot: StreamBot, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Var.BIN_CHANNEL is not None:
            await bot.send_message(
                int(Var.BIN_CHANNEL),
                f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{(await bot.get_me()).username} !!"
            )

