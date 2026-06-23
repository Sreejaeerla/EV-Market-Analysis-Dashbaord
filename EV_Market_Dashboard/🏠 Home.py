import streamlit as st
from utils.styles import local_css
import base64
import pandas as pd
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EV Market Analysis Dashboard",
    page_icon="🚗",
    layout="wide"
)

local_css()

# ---------------- LOAD DATA ----------------
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "1.data", "cleaned_EV_Dataset3.xls")
df = pd.read_csv(file_path)

# ------------ LOAD IMAGE AS BASE64 ------------
img_path = os.path.join(base_dir, "images", "e_car.avif")
with open(img_path, "rb") as img_file:
    img = base64.b64encode(img_file.read()).decode()

# ---------------- HERO SECTION ----------------
st.markdown(
f"""
<style>

/* Header transparent again — shows exactly what's behind it, no color-guessing/seam */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

/* Lock the page — no scrolling, on every layer that could scroll independently */
html, body {{
    overflow: hidden;
}}

[data-testid="stAppViewContainer"] {{
    overflow: hidden;

    /* Background image back on the full app container so it sits behind the header too */
    background:
    linear-gradient(
        rgba(0,0,0,0.35),
        rgba(0,0,0,0.35)
    ),
    url("data:image/jpg;base64,{img}");

    background-size: cover;
    background-position: calc(50% + 160px) center;
    background-repeat: no-repeat;
}}

[data-testid="stMain"] {{
    overflow: hidden;
}}

/* Remove default spacing */
.block-container {{
    padding-top: 0rem !important;
    padding-left: 0rem;
    padding-right: 0rem;
    padding-bottom: 0rem !important;
    position: relative;
}}

.hero {{
    height: calc(100vh - 3.75rem);
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    transform: translateY(-50px);
}}

.hero h1 {{
    color: white;
    font-size: 75px;
    font-weight: bold;
}}

.hero p {{
    color: white;
    font-size: 28px;
    line-height: 1.8;
}}

div[data-testid="stHorizontalBlock"]:has(div[data-testid="stButton"]) {{
    position: absolute;
    top: calc(100vh - 200px);
    left: 0;
    width: 100%;
    z-index: 999;
    display: flex;
    justify-content: center;
    align-items: center;
    transform: translate(40px, -30px);
}}

div[data-testid="stHorizontalBlock"]:has(div[data-testid="stButton"]) > div[data-testid="column"] {{
    flex: none !important;
    width: auto !important;
}}

div[data-testid="stButton"] > button {{
    background-color: transparent;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 18px;
    padding: 14px 36px;
    border-radius: 8px;
    border: 2px solid #FFFFFF;
    cursor: pointer;
    transition: all 0.2s ease;
}}

div[data-testid="stButton"] > button:hover {{
    background-color: rgba(255, 255, 255, 0.12);
    transform: scale(1.03);
}}

div[data-testid="metric-container"]{{
    background-color:#1B4332;
    border:1px solid #00E676;
    padding:20px;
    border-radius:15px;
    text-align:center;
}}

div[data-testid="stMetricLabel"] p{{
    font-size:28px !important;
    font-weight:bold !important;
    color:white !important;
}}

div[data-testid="stMetricValue"]{{
    font-size:28px !important;
    font-weight:bold !important;
}}

.feature-box {{
    background-color: #1B4332;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #00E676;
    text-align: center;
    min-height: 220px;
}}

</style>
""",
unsafe_allow_html=True
)

# ---------------- HERO ----------------
st.markdown(
"""
<div class="hero">

<h1>⚡ EV Market Analysis Dashboard</h1>

<h2 style="
color:white;
font-size:38px;
font-weight:600;
margin-top:10px;
">
Explore Electric Vehicle Performance
</h2>

<h3 style="
color:white;
font-size:28px;
font-weight:400;
line-height:1.8;
">
Range Analysis • Charging • Efficiency • Pricing • Market Trends
</h3>

</div>

""",
unsafe_allow_html=True
)

# ---------------- BUTTON ----------------
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Let's Explore", key="explore_dashboard_btn"):
        st.switch_page("pages/2_📖_About_Project.py")
