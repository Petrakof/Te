import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.error import URLError
from transformers import pipeline


st.markdown("# Анализ тональности такста")
st.sidebar.markdown( "Анализ тональности такста")

@st.cache(allow_output_mutation=True)
DATA = ('df.csv')

# Создадим функцию для загрузки данных
def load_model():
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    return model

st.header ("Определение тональности текстов")

result = st.button("Определить тональность текста")
model = load_model()
if result:
    res = model(text)
    sent = res[0]['label'] 
    st.write(model(text)[0]["label"])