import streamlit as st
import numpy as np
import pandas as pd
from transformers import pipeline
from PIL import  Image

# Title of the application 
st.title('Анализ тональности чатов Телеграм\n', )
st.subheader("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

display = Image.open('images/display.jpg')
display = np.array(display)
st.image(display)

# Sidebar options
option = st.sidebar.selectbox('выбрать из списка', 
["Добро Пожаловать",
 "Определение тональности текста", 
  "Word Cloud", 
 ])

st.set_option('deprecation.showfileUploaderEncoding', False)

if option == 'ГДобро Пожаловать':
	st.write(
			"""
				## Описание проекта
				Это инструмент анализа текста, разработанный группой 32. Доступ к инструментам можно получить на левой боковой панели.
			"""
		)
elif option == "Определение тональности текста":

 @st.cache(allow_output_mutation=True)
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