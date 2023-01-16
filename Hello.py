import numpy as np
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

page_names_to_funcs = {
    "—": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
