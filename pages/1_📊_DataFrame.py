import streamlit as st
import pandas as pd
from urllib.error import URLError
from transformers import pipeline
import plotly_express as px

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame")
st.sidebar.header("DataFrame)
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames"""
)

@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")