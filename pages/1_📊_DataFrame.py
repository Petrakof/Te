import streamlit as st
import pandas as pd
from urllib.error import URLError
from transformers import pipeline


st.set_page_config(page_title="DataFrame", page_icon="📊")

st.markdown("# DataFrame")
st.sidebar.header("DataFrame")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames"""
)


