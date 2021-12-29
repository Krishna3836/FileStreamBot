# (c) @AbirHasan2005

import time
import string
import random
import asyncio
import datetime
import aiofiles
import traceback
import aiofiles.os
from Code_X_Mania.vars import Var
from Code_X_Mania.database import db
from pyrogram.types import Message
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

broadcast_ids = {}


async def send_msg(user_id, message):
    try:
        if Var.BROADCAST_AS_COPY is False:
            await message.forward(chat_id=user_id)
        elif Var.BROADCAST_AS_COPY is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"




