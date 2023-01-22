import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np



#загружаю модель
@st.cache
def read_data(uploaded_file):
    return pd.read_csv(uploaded_file)

datafile = st.sidebar.file_uploader("Загрузите файл csv", ["csv"])
if datafile is None:
    st.info("""Загрузите набор данных (.csv) на боковой панели, чтобы приступить к работе.""")
    st.stop()

data = read_data(datafile).copy()
dat = data.dropna(axis='index', how='any', subset=['text'])

#обучение модели
model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
                      
result = st.sidebar.button('🤗Распознать')

df_model = dat.copy()

if result:
    lst = []
    for i in df_model["text"]:
        lst.append(model(str(i))[0]["label"])
        df_model["Sentinent"]=pd.DataFrame(lst)


#Это вкладки
tab1, tab2 = st.tabs(["Загруженные данные", "Данные после обучения"])

tab1.subheader("Загруженные данные")
tab1.write(data)

tab2.subheader("Данные после обучения")

with tab2:
    with st.expander("Все сообщения"):
        st.write(df_model)
    with st.expander("🙁 Негативные сообщения"):
        st.write(df_model[df_model["Sentinent"]=="NEGATIVE"])
    with st.expander("🙃 Позитивные  сообщения"):
        st.write(df_model[df_model["Sentinent"]=="POSITIVE"])
    with st.expander("Нейтральные сообщения"):
        st.write(df_model[df_model["Sentinent"]=="NEUTRAL"])

