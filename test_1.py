import streamlit as st
from transformers import pipeline

st.header("Определение тональности текстов")
st.subheader("Введите текст для анализа")

text = st.text_area(" ",height=100)

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

result = st.button('Распознать текст')

def classif(txt):
  return classifier(txt)[0]["label"]

st.write ("Тональность текста:")
st.write(classif(text))

def test_classif_1():
  s = classif("Я люблю снег")
  assert s == 'POSITIVE'
  
def test_classif_2():
  s = classif("Я ненавижу снег")
  assert s == 'NEGATIVE'
  
def test_classif_3():
  s = classif("Зима")
  assert s == 'NEUTRAL'
