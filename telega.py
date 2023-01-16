#import numpy as np
import streamlit as st
from transformers import pipeline
from PIL import  Image
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the application 
st.title('Анализ тональности текста\n', )
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

# Sidebar options
option = st.sidebar.selectbox('выбрать из списка', 
["# Добро пожаловать! 👋",
 "Определение тональности текста", 
  "Word Cloud", 
 ])

st.set_option('deprecation.showfileUploaderEncoding', False)

if option == '# Добро пожаловать! 👋':
	st.write(
			"""
				## Описание проекта
				Это инструмент анализа текста, разработанный группой 32. Доступ к инструментам можно получить на левой боковой панели.
			"""
		)
elif option == "Определение тональности текста":



 def read_data(uploaded_file):
    return pd.read_csv(uploaded_file)

datafile = st.sidebar.file_uploader("Загрузите файл csv", ["csv"])
if datafile is None:
    st.info("""Загрузите набор данных (.csv) на боковой панели, чтобы приступить к работе.""")
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