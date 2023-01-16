import streamlit as st
import pandas as pd
from urllib.error import URLError
from transformers import pipeline
import plotly.express as px

st.markdown("# История чата Телеграм 🎉")

st.sidebar.markdown("# История чата Телеграм 🎉")
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

def load_model_2():
    model_2=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    return model_2

st.header ("Определение тональности текстов")
df_model = df.copy()
load_model_2(df_model["text"][1])[0]["label"]

lst = []
for i in df_model["text"]:
  lst.append(load_model_2(str(i))[0]["label"])
df_model["Sentinent"]=pd.DataFrame(lst)
df_model