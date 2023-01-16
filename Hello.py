import numpy as np
import streamlit as st
from transformers import pipeline
from PIL import  Image
from telethon.sync import TelegramClient

def intro(): 
     import streamlit as st
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

page_names_to_funcs = {
    "—": intro,
    "1_📊_DataFrame": 1_📊_DataFrame,
    "2_Анализ тональности текста": 2_Анализ тональности текста,
    "3_Диаграммы": Диаграммы
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
