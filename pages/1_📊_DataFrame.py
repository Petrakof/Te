import streamlit as st
import pandas as pd
from urllib.error import URLError
from transformers import pipeline
import plotly.express as px

DATA = ('df.csv')

@st.cache # для оптимизации работы приложения

# Создадим функцию для загрузки данных
def load_data():
    df = pd.read_csv(DATA)
    return df   
df = load_data() 

show_data = st.sidebar.success('Show raw data')
if show_data == True:
    st.subheader('Raw data')
    
    st.write(df)
