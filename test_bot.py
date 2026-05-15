import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ButtonStyle

logging.basicConfig(level=logging.WARNING)

API_ID = 38674666
API_HASH = "b4f0fbf8fb560c4bc9e7b9f3698e474c"
BOT_TOKEN = "8795355233:AAF9Ly9bzbN4YH9wpeRQSZ62zSP3dqgWfsc"
CUSTOM_EMOJI_ID = 5238162283368035495

app = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.all & filters.incoming)
async def any_message(client, message):
    await message.reply(
        "✅ Test Message",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Approve", callback_data="approve", style=ButtonStyle.SUCCESS, emoji_icon=CUSTOM_EMOJI_ID),
                InlineKeyboardButton("Reject", callback_data="reject", style=ButtonStyle.DANGER, emoji_icon=CUSTOM_EMOJI_ID)
            ]
        ])
    )
    print("🔥 SENT!")

app.run()
