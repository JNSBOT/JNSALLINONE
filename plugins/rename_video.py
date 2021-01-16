#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Jega Turbo

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time
import random
import asyncio
# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
#from pyrogram import Client, Filters
from helper_funcs.help_Nekmo_ffmpeg import take_screen_shot
from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image
#from database.database import *
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

async def force_name(bot, message):

    await bot.send_message(
        message.reply_to_message.from_user.id,
        "Enter new name for media\n\nNote : Extension not required",
        reply_to_message_id=message.reply_to_message.message_id,
        reply_markup=ForceReply(True)
    )

@Client.on_message(filters.private & filters.reply & filters.text)
async def cus_name(bot, message):
    
    if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        asyncio.create_task(rename_doc(bot, message))     
    else:
        print('No media present')

    
async def rename_doc(bot, message):
    
    mssg = await bot.get_messages(
        message.chat.id,
        message.reply_to_message.message_id
    )    

    media = mssg.reply_to_message

    
    if media.empty:
        await message.reply_text('Why did you delete that 😕', True)
        return
        
    filetype = media.document or media.video or media.audio or media.voice or media.video_note
    try:
        actualname = filetype.file_name
        splitit = actualname.split(".")
        extension = (splitit[-1])
    except:
        extension = "mkv"

    await bot.delete_messages(
        chat_id=message.chat.id,
        message_ids=message.reply_to_message.message_id,
        revoke=True
    )
    
    if message.from_user.id not in Config.BANNED_USERS:
        file_name = message.text

#@pyrogram.Client.on_message(pyrogram.Filters.command(["rename_video"]))
#async def rename_video(bot, update):
    #if update.from_user.id in Config.BANNED_USERS:
        #await bot.delete_messages(
            #chat_id=update.chat.id,
            #message_ids=update.message_id,
            #revoke=True
        #)
        #return
    #TRChatBase(update.from_user.id, update.text, "rename_video")
    #if (" " in update.text) and (update.reply_to_message is not None):
        #cmd, file_name = update.text.split(" ", 1)
        #if len(file_name) > 512:
            #await update.reply_text(
                #Translation.IFLONG_FILE_NAME.format(
                    #alimit="512",
                    #num=len(file_name)
                #)
            #)
            #return
        description = Translation.CUSTOM_CAPTION_UL_FILE
        download_location = Config.DOWNLOAD_LOCATION + "/"
        b = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_START,
                b,
                c_time
            )
        )
        if the_real_download_location is not None:
            try:
                await bot.edit_message_text(
                    text=Translation.SAVED_RECVD_DOC_FILE,
                    chat_id=update.chat.id,
                    message_id=b.message_id
                )
            except:
                pass
            new_file_name = download_location + file_name
            os.rename(the_real_download_location, new_file_name)
            await bot.edit_message_text(
                text=Translation.UPLOAD_START,
                chat_id=update.chat.id,
                message_id=b.message_id
                )
            logger.info(the_real_download_location)
            width = 0
            height = 0
            duration = 0
            metadata = extractMetadata(createParser(new_file_name))
            try:
             if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            except:
              pass
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
               try:
                    thumb_image_path = await take_screen_shot(new_file_name, os.path.dirname(new_file_name), 7)
               except:
                    thumb_image_path = await take_screen_shot(new_file_name, os.path.dirname(new_file_name), 0)
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                # resize image
                # ref: https://t.me/PyrogramChat/44663
                # https://stackoverflow.com/a/21669827/4723940
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                # https://stackoverflow.com/a/37631799/4723940
                # img.thumbnail((90, 90))
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")
                # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            c_time = time.time()
            await bot.send_video(
                chat_id=update.chat.id,
                video=new_file_name,
                duration=duration,
                thumb=thumb_image_path,
                caption=f"<b>{file_name}</b>",
                # reply_markup=reply_markup,
                reply_to_message_id=update.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.UPLOAD_START,
                    b, 
                    c_time
                )
            )
            try:
                os.remove(new_file_name)
                #os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=update.chat.id,
                message_id=b.message_id,
                disable_web_page_preview=True
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.REPLY_TO_DOC_FOR_RENAME_FILE,
            reply_to_message_id=update.message_id
        )
