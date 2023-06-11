from telethon import TelegramClient
import sqlite3, time, sys
from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageEntityTextUrl
import requests
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def get_client(api_id, api_hash, session_name):
    try:
        client = TelegramClient(session_name, api_id, api_hash)
        return client

    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
        print("Retrying...")
        sys.exit()

# Get all urls from telegram channels messages
async def get_msg(channel_username, client):

    await client.start()
    channel = await client.get_entity(channel_username)
    urls = []

    async for message in client.iter_messages(channel, limit=500):
        entities = message.entities
        if entities:
            for entity in entities:
                if isinstance(entity, MessageEntityTextUrl):
                    urls.append(entity.url)

    await client.disconnect()
    return urls

# Get all urls from telegram channels messages
def get_last_msg(api_id, api_hash, session_name, channel_username):
    loop = asyncio.new_event_loop() # Create a new event loop
    client = loop.run_until_complete(get_client(api_id, api_hash, session_name))
    urls = loop.run_until_complete(get_msg(channel_username, client))
    loop.close()

    return urls

def send_msg(msg, channel, BOT_TOKEN):

    send_text = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel}&parse_mode=Markdown&text={msg}'
    response = requests.get(send_text)

    return response
