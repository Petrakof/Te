import numpy as np
import pandas as pd
import streamlit as st
from transformers import pipeline
from PIL import  Image
from telethon.sync import TelegramClient


st.set_page_config(
    page_title="Добро пожаловать",
    page_icon="👋",)
# Title of the application 
st.write("# Добро пожаловать! 👋")

st.sidebar.success("Select a demo above.")
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

display = Image.open('images/display.jpg')
display = np.array(display)
st.image(display)

@st.cache
def read_data(uploaded_file):
    return pd.read_csv(uploaded_file)

datafile = st.sidebar.file_uploader("Загрузите файл csv", ["csv"])
if datafile is None:
    st.info("""Загрузите набор данных (.csv) на боковой панели, чтобы приступить к работе.""")
    st.stop()

data = read_data(datafile).copy()

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