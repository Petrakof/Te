import streamlit as st
import numpy as np
import pandas as pd
from transformers import pipeline
import asyncio
import ctypes.util
from xmlrpc.client import DateTime
import telethon
from telethon.sync import TelegramClient
from telethon import connection
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
 
import csv


async def main():
    client = TelegramClient(
     phone=st.text_input ("Введите свой номер телефона", "89112166840"), 
     api_id=st.text_input ('Введите свой api_id: ',"29319788"  ),
     api_hash= st.text_input ('Введите свой api_hash: ', 'a0c785ad0fd3e92e7c131f0a70987987'))
     await client.start()
asyncio.run(main())


code=st.text_input ("Введите свой номер код", "")

name=st.text_input ("Введите свой номер код", "Настя")

chat=st.text_input ("Введите свой номер код", "t.me/+KxlX36pb-3hjMjRi")

data = [] 

with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(chat, limit=100):
        data.append([message.from_id.user_id, message.text])


df = pd.DataFrame(data, columns=['user_id', 'text'])

