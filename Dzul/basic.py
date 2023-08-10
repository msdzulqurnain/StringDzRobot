from assets.strings.id import ID
from assets.button import BUTTON
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(
        msg.chat.id,
        ID.START_TEXT.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(BUTTON.BHOME)
    )


# Help Message
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id, ID.HELP_TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON.BACK)
    )


# About Message
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id,
        ID.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(BUTTON.BACK),
    )
