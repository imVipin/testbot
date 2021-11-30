import os
from pyrogram import Client, filters
#import ytthumb
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from telegraph import upload_file

UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "pdfmalayalam")

@Client.on_message(filters.command(["telegraph"]))
async def uploadphoto(client, message):
    if update.reply_to_message is not None:
      msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
      userid = str(message.chat.id)
      img_path = (f"./DOWNLOADS/{userid}.jpg")
      img_path = await client.download_media(message=message, file_name=img_path)
      await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
      try:
        tlink = upload_file(img_path)
      except:
        await msg.edit_text("`Something went wrong`") 
      else:
        await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
        os.remove(img_path) 	
    else:
      await bot.send_message(text="reply  with photo image")
            

