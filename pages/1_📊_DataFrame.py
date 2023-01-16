import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame")
st.sidebar.header("DataFrame)
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames"""
)