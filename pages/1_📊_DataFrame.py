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
def read_data(uploaded_file):
    return pd.read_csv(uploaded_file)

datafile = st.sidebar.file_uploader("Загрузите файл csv", ["csv"])
if datafile is None:
    st.info("""Загрузите набор данных (.csv) на боковой панели, чтобы приступить к работе.""")
    st.stop()
    
  