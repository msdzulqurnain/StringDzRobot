from env import FSUB
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def FSUB(bot: Client, msg: Message):
    if not FSUB:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(FSUB, msg.from_user.id)
        except UserNotParticipant:
            if FSUB.isalpha():
                link = "https://t.me/" + FSUB
            else:
                chat_info = await bot.get_chat(FSUB)
                link = chat_info.invite_link
            try:
                nama = msg.from_user.first_name
                namalu = msg.from_user.last_name
                await msg.reply(
                    text=FSUB_TEXT.format(nama, namalu),
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Join Disini", url="https://t.me/DezetSupport")],
                        [InlineKeyboardButton("Join Disini", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {FSUB} !")
