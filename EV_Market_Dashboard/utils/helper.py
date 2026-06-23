import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("1.data/cleaned_EV_Dataset3.xls")
    return df