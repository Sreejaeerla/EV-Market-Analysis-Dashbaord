import streamlit as st

def local_css():

    st.markdown("""
    <style>

    /* Main app background */
    .stApp{
        background-color:#0B1F17;
    }

    /* Transparent top header */
    header{
        background: transparent;
    }

    [data-testid="stHeader"]{
        background: rgba(0,0,0,0);
    }

    /* Remove top decoration line */
    [data-testid="stDecoration"]{
        display:none;
    }

    /* Keep toolbar visible */
    [data-testid="stToolbar"]{
        right:1rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background-color:#1B4332;
    }

    /* Sidebar navigation — bold page names */
    [data-testid="stSidebarNav"] a{
        font-weight:700;
    }

    /* Headings */
    h1{
        color:#00E676;
    }

    h2, h3{
        color:#7CFC00;
    }

    /* Metric cards */
    div[data-testid="metric-container"]{
        background-color:#1B4332;
        border:1px solid #00E676;
        padding:15px;
        border-radius:15px;
    }

    /* Sidebar metric labels */
    section[data-testid="stSidebar"] [data-testid="stMetricLabel"]{
        font-size:12px !important;
        font-weight:400 !important;
        color:rgba(255,255,255,0.7) !important;
    }

    /* Sidebar metric values */
    section[data-testid="stSidebar"] [data-testid="stMetricValue"]{
        font-size:16px !important;
        font-weight:600 !important;
        color:white !important;
        line-height:1.3;
    }

    /* ===== FILTER DROPDOWNS ===== */
    [data-testid="stSidebar"] div[data-baseweb="select"] > div{
        background: rgba(0, 230, 118, 0.12) !important;
        border: 1px solid #1B4332 !important;
        box-shadow: none !important;
        outline: none !important;
        border-radius: 10px !important;
    }

    /* Remove blue focus border */
    [data-testid="stSidebar"] div[data-baseweb="select"]:focus-within > div{
        border: 1px solid #1B4332 !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* Filter text */
    [data-testid="stSidebar"] div[data-baseweb="select"] span{
        color: white !important;
    }

    /* Filter labels */
    [data-testid="stSidebar"] label{
        color:white !important;
        font-weight:600 !important;
    }

    /* Selected tag — muted soft green instead of bright green */
    [data-testid="stSidebar"] span[data-baseweb="tag"] {
        background-color: rgba(0, 180, 90, 0.25) !important;
        border: 1px solid rgba(0, 200, 100, 0.40) !important;
        color: rgba(255, 255, 255, 0.90) !important;
    }

    </style>
    """, unsafe_allow_html=True)