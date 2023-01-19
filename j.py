import streamlit as st
import numpy as np
import pandas as pd
from transformers import pipeline
from xmlrpc.client import DateTime
from telethon.sync import TelegramClient
 
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
 
import csv
api_id= st.text_input() 
api_hash = st.text_input('') 
phone = st.text_input('')
 
client = TelegramClient(phone, api_id, api_hash)
 
client.start()
