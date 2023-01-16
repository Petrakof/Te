import numpy as np
import streamlit as st
from transformers import pipeline
from PIL import  Image
st.set_page_config(
    page_title="Анализ тональности текста",
    page_icon="👋",)
# Title of the application 
st.write("# Добро пожаловать! 👋")

st.sidebar.success("Select a demo above.")
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")