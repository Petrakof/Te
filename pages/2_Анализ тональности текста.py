import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.error import URLError
from transformers import pipeline
from telethon.sync import TelegramClient


st.markdown("# Анализ тональности такста")
st.sidebar.markdown( "Анализ тональности такста")

@st.cache(allow_output_mutation=True)
df_model = df.copy()
# Создадим функцию для загрузки данных
def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    model(df_model["text"][1])[0]["label"]

    return model
model = load_model()
st.header ("Определение тональности текстов")
st.subheader ("Введите текст для анализа")
text = st.text_area(" ",height=100)
result = st.button("Определить тональность текста")
df_model

