import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    # Works both locally and on Streamlit Cloud
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "1.data", "cleaned_EV_Dataset3.xls")
    df = pd.read_csv(file_path)
    return df
