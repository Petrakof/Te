import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.error import URLError
from transformers import pipeline


st.markdown("# Анализ тональности такста")
st.sidebar.markdown( "Анализ тональности такста")

@st.cache(allow_output_mutation=True)

# Создадим функцию для загрузки данных
def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    return model

st.header ("Определение тональности текстов")
df_model = df.copy()
lst = []
for i in df_model["text"]:
  lst.append(model(str(i))[0]["label"])
df_model["Sentinent"]=pd.DataFrame(lst)
df_model
result = st.button("Определить тональность текста")
