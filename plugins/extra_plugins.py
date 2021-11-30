import os
from pyrogram import Client, filters
#import ytthumb
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from telegraph import upload_file

UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "pdfmalayalam")

@Client.on_message(filters.command(["info"]))
async def telegraph_upload(bot, update):
    #if not await db.is_user_exist(update.from_user.id):
	    #await db.add_user(update.from_user.id)
    if UPDATE_CHANNEL:
        try:
            user = await bot.get_chat_member(UPDATE_CHANNEL, update.chat.id)
            if user.status == "kicked":
                await update.reply_text(text="You are banned!")
                return
        except UserNotParticipant:
            await update.reply_text(
		  text="Join my pdf channel to use me",
		  reply_markup=InlineKeyboardMarkup(
			  [[InlineKeyboardButton(text="⚙ Join Updates Channel ⚙", url=f"https://telegram.me/{UPDATE_CHANNEL}")]]
		  )
	    )
            return
        except Exception as error:
            print(error)
            await update.reply_text(text="Something wrong. Contact Developer.", disable_web_page_preview=True)
            return
    medianame = "./DOWNLOADS/" + "Vipinpkd/FindPDFBot"
    text = await update.reply_text(
        text="<code>Downloading to My Server ...</code>",
        disable_web_page_preview=True
    )
    await bot.download_media(
        message=update,
        file_name=medianame
    )
    await text.edit_text(
        text="<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>",
        disable_web_page_preview=True
    )
    try:
        response = upload_file(medianame)
    except Exception as error:
        print(error)
        await text.edit_text(
            text=f"Error :- {error}",
            disable_web_page_preview=True
        )
        return
    try:
        os.remove(medianame)
    except Exception as error:
        print(error)
        return
    await text.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [InlineKeyboardButton(text="⚙ Join Updates Channel ⚙", url="https://telegram.me/pdfmalayalam")]
            ]
        )
    )
