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

show_data = st.sidebar.checkbox('Show raw data')
if show_data == True:
    st.subheader('Raw data')
    
    st.write(df)

@st.cache(allow_output_mutation=True)

def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    return model

model = load_model()
df_model = df.copy()
st.header ("Определение тональности текстов")
st.subheader ("Введите текст для анализа")
text = df_model["text"][1])[0]["label"]
result = st.button("Определить тональность текста")