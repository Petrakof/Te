import streamlit as st
import pandas as pd
from urllib.error import URLError
from transformers import pipeline
import plotly.express as px

st.set_page_config(page_title="DataFrame", page_icon="📊")

st.markdown("# DataFrame")
st.sidebar.header("DataFrame")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames"""
)

DATA = ('df.csv')


@st.cache # для оптимизации работы приложения

# Создадим функцию для загрузки данных
def load_data():
    df = pd.read_csv(DATA)
    return df   

# Применим функцию 
df = load_data() 

if show_data == True:
    st.subheader('Raw data')
    
    st.write(df)
