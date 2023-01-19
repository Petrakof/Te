import streamlit as st
import numpy as np
import pandas as pd
from transformers import pipeline

from xmlrpc.client import DateTime
import telethon
from telethon.sync import TelegramClient
 
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
 
import csv
 
api_id=st.text_input ('Введите свой api_id: ',"  "  )
api_hash = st.text_input ('Введите свой api_hash: ', ' a0c785ad0fd3e92e7c131f0a70987987')

phone = st.text_input ("Введите свой номер телефона", "  ")

async def main():
    client = TelegramClient(phone, api_id, api_hash)
    await client.start()
result = st.button('Распознать')

name= st.text_input
name= st.text_input
name= st.text_input ("Введите свой ник в Телеграм", "Настя")
code= st.text_input ("Введите свой код", "    ")



