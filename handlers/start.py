from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJchtgfvsZvz3OOIlXFLoLmSayvZsRrAACdgEAAi296UdEmIVdxe3iSR8E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your group's voice chatππ₯
**A perfect Music Player...**
\nTo add in your group contact us at @akari_support.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βͺ SUPPORT GROUP βͺ", url="https://t.me/akari_support",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "βͺ CHANNEL βͺ", url="https://t.me/AkariSupport"
                    ),
                    InlineKeyboardButton(
                        "βͺ CREATOR βͺ", url="https://t.me/ThesedLyf"
                    ),
                    InlineKeyboardButton(
                        "ποΈ COMMAND ποΈ", url="https://telegra.ph/Akari-Music-Bot-04-20"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β Add To Your Group β", url="https://t.me/Akari_MusicBoT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
