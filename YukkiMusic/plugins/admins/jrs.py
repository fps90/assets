from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@app.on_message(
    command(["السورس", "سورس", "المبرمج"])
)
async def mak(client: Client, message: Message):
    await message.reply_photo(
        photo="https://i.ibb.co/HnC5B2R/image.jpg",
        caption="~ Team freedom \n~ Dav Poker",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦗ Dev ⦘", url="https://t.me/vvvv00"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⦗ Updates ⦘", url="https://t.me/issss9"
                    ),
                    InlineKeyboardButton(
                        "⦗ support ⦘", url="https://t.me/issss9"
                    ),
                ],
            ]
        ),
    )
