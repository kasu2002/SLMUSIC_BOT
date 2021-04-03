# epusthakalaya bots <https://t.me/e_pusthakalaya>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SLMUSICBOT.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SLMUSICBOT import Jebot as app
from SLMUSICBOT import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot 🎵

Just send me the song name you want to download.
eg: ```/song Satisfya```

A bot by @e_pusthakalaya
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Source", url="https://github.com/ImJanindu/JESongBot"
                    ),
                    InlineKeyboardButton(
                        text="Dev", url="https://t.me/ImJanindu"
                    ),
                     InlineKeyboardButton(
                        text="edit by", url="https://https://t.me/kasu_bro"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("SLMUSICBOT is online.")
idle()
