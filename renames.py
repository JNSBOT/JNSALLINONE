from telethon import TelegramClient, events, Button
    #import requests
from bs4 import BeautifulSoup as BS

import asyncio

import subprocess

import requests

#from headers import headers

#import urls

import os
import subprocess

import cryptg

import youtube_dl

import logging
logging.basicConfig(level=logging.WARNING)
client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
@client.on(events.NewMessage(pattern=".*/renames"))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    print(links)
  #  print("hi")
    with open("./Download/"+links, 'wb') as fd:
        async for chunk in client.iter_download(dw.media):
            fd.write(chunk)
            print("hh")
    await client.send_message(chat,links,file="./Download/"+links,force_document=True)
    os.remove("./Download/"+links)

client.start()

client.run_until_disconnected()
