import numpy as np
import streamlit as st
from transformers import pipeline
from PIL import  Image
import plotly_express as px

st.set_page_config(
    page_title="Добро пожаловать",
    page_icon="👋",)
# Title of the application 
st.write("# Добро пожаловать! 👋")

st.sidebar.success("Начало")
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")