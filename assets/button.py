from pyrogram.types import InlineKeyboardButton


class BUTTON:
    BBUAT = [InlineKeyboardButton("🔥Start Generating Session🔥", callback_data="generate")]

    BACK = [
        generate_single_button,
        [InlineKeyboardButton(text="Kembali", callback_data="home")]
    ]

    generate_button = [BBUAT]

    BHOME = [
        BBUAT,
        [InlineKeyboardButton("Support", url="https://t.me/DezetSupport")],
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("OWNER", url="https://t.me/msdqqq")],
    ]
