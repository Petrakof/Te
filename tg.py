import streamlit as st
import pandas as pd
from telethon import TelegramClient


api_id=st.text_input("api_id",'___'   ) 
api_hash=st.text_input ("Введите свой нa api_hash", '___') 
phone= st.text_input ("Введите свой номер телефона", '___') 

result = st.button('🤗Распознать')

client = TelegramClient(phone, api_id, api_hash)
 
client.start()

code = st.text_input("code", '___' ) 

name = st.text_input("name", '___' ) 
chat =st.text_input("chat", '___' ) 

data = [] 

with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(chat, limit=100):
        data.append([message.from_id.user_id, message.text])


df = pd.DataFrame(data, columns=['user_id', 'text'])
result = st.button(df)

