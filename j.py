import streamlit as st
import numpy as np
import pandas as pd
from transformers import pipeline
import asyncio
import ctypes.util
import configparser
from xmlrpc.client import DateTime
import telethon
from telethon.sync import TelegramClient
from telethon import connection
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import csv

# this def gets called when the /telethon command is sent by the user to the bot
def telethonMessage(update, context):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    api_id =st.text_input ('API_ID')
    api_hash = st.text_input('API_HASH')
    client = TelegramClient('anon', api_id, api_hash, loop=loop)
    with client:
        loop.run_until_complete(send_telethon_message(client, update.effective_user.id))
     

async def send_telethon_message(client, user_id):
    me = await client.get_me()
    print('TELETHON: {}', me.username)
    await client.send_message(user_id, 'Testing Telethon')


