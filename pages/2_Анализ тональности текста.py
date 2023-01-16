import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.error import URLError
from transformers import pipeline
from telethon.sync import TelegramClient


st.markdown("# Анализ тональности такста")
st.sidebar.markdown( "Анализ тональности такста")

@st.cache(allow_output_mutation=True)
#
# Создадим функцию для загрузки данных
def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
                      
result = st.sidebar.button('Распознать')

df_model = data.copy()

if result:
    lst = []
    for i in df_model["text"]:
        lst.append(model(str(i))[0]["label"])
        df_model["Sentinent"]=pd.DataFrame(lst)

st.write(df_model)
