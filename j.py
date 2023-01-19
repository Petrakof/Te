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
 
api_id=st.text_input ('Введите свой api_id: ', ' 29319788')
api_hash = st.text_input ('Введите свой api_hash: ', ' a0c785ad0fd3e92e7c131f0a70987987')

phone = st.text_input ("Введите свой номер телефона", "    ")

name= st.text_input ("Введите свой ник в Телеграм", "Настя")

async def main():
    client = TelegramClient(phone, api_id, api_hash)
    assert await client.connect()

code= st.text_input ("Введите свой код", "    ")



