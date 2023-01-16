import streamlit as st
import pandas as pd
from transformers import pipeline

@st.cache
def read_data(uploaded_file):
    return pd.read_csv(uploaded_file)

datafile = st.file_uploader("Загрузите файл csv", ["csv"])
if datafile is None:
    st.info("""Загрузите набор данных (.csv), чтобы приступить к работе.""")
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