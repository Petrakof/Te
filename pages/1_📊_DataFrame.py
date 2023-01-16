import streamlit as st
import pandas as pd
from urllib.error import URLError
from transformers import pipeline
import plotly.express as px
from telethon.sync import TelegramClient

st.markdown("# История чата Телеграм 🎉")

st.sidebar.markdown("# История чата Телеграм 🎉")
DATA = ('df.csv')

@st.cache # для оптимизации работы приложения

# Создадим функцию для загрузки данных
def load_data():
    df = pd.read_csv(DATA)
    return df   
df = load_data() 

show_data = st.sidebar.checkbox('Show raw data')
if show_data == True:
    st.subheader('Raw data')
    
    st.write(df)
df_model = df.copy()
def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    model(df_model["text"][1])[0]["label"]
  
    lst = []
    for i in df_model["text"]:
         lst.append(model(str(i))[0]["label"])
    df_model["Sentinent"]=pd.DataFrame(lst)
    df_model
    return model
df_model
