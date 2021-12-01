import os
from pyrogram import Client, filters
#import ytthumb
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from telegraph import upload_file

UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "pdfmalayalam")

