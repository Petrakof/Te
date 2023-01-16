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
df = pd.read_csv("df.csv")

@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

