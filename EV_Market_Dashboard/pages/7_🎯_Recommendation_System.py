import streamlit as st
from utils.helper import load_data
from utils.styles import local_css

local_css()

df = load_data()

st.markdown("""
<style>

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse at 80% 10%, rgba(0,230,118,0.10) 0%, transparent 50%),
        radial-gradient(ellipse at 10% 80%, rgba(0,100,255,0.08) 0%, transparent 50%),
        linear-gradient(135deg, #050f1a 0%, #0a1f14 50%, #050f1a 100%);
    background-attachment: fixed;
}

html, body { overflow: auto; }
[data-testid="stAppViewContainer"],
[data-testid="stMain"] { overflow: auto; }

.block-container {
    padding-top: 0rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-bottom: 3rem !important;
    max-width: 100% !important;
}

.glass {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 18px;
    padding: 28px 34px;
    margin-bottom: 16px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    width: 100%;
    box-sizing: border-box;
}

.glass-title {
    color: #ffffff;
    font-size: 22px;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 16px;
}

[data-testid="stSlider"] {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 18px;
    padding: 20px 28px !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    margin-bottom: 16px;
}

[data-testid="stSlider"] label p {
    color: rgba(255, 255, 255, 0.95) !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

/* Scrollable table wrapper — fixed height like st.dataframe */
.table-scroll {
    height: 400px;
    overflow-y: auto;
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Scrollbar styling */
.table-scroll::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
.table-scroll::-webkit-scrollbar-track {
    background: rgba(255,255,255,0.04);
    border-radius: 4px;
}
.table-scroll::-webkit-scrollbar-thumb {
    background: rgba(0,230,118,0.35);
    border-radius: 4px;
}

.ev-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

/* Sticky header so it stays visible while scrolling */
.ev-table thead tr th {
    position: sticky;
    top: 0;
    z-index: 2;
    background-color: #1e3a2e !important;
    color: rgba(255,255,255,0.75) !important;
    font-weight: 600;
    font-size: 12px;
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid rgba(255,255,255,0.10);
    letter-spacing: 0.03em;
    white-space: nowrap;
}

.ev-table tbody td {
    background-color: #132a1f;
    color: rgba(255,255,255,0.88);
    padding: 7px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    font-size: 13px;
    white-space: nowrap;
}

.ev-table tbody tr:hover td {
    background-color: #1e3d2c;
}

h1 { color: white !important; }

.footer-text {
    color: rgba(255,255,255,0.25);
    font-size: 13px;
    text-align: center;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------
st.sidebar.header("Filters")

selected_brands = st.sidebar.multiselect(
    "Brand",
    options=sorted(df["brand_name"].unique()),
    placeholder="Choose brand name"
)
selected_segments = st.sidebar.multiselect(
    "Market Segment",
    options=sorted(df["market_segment"].unique()),
    placeholder="Choose market segment"
)
selected_drive = st.sidebar.multiselect(
    "Drive Type",
    options=sorted(df["drive_type"].unique()),
    placeholder="Choose drive type"
)

filtered_df = df.copy()
if selected_segments:
    filtered_df = filtered_df[filtered_df["market_segment"].isin(selected_segments)]
if selected_drive:
    filtered_df = filtered_df[filtered_df["drive_type"].isin(selected_drive)]
if selected_brands:
    filtered_df = filtered_df[filtered_df["brand_name"].isin(selected_brands)]

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.markdown("""
<div style="text-align:center; margin-top:0px; margin-bottom:20px;">
    <span style="
        color: #ffffff;
        font-size: 36px;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.1;
        display: inline-block;
    ">EV Recommendation System</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sliders
# ---------------------------------------------------
budget = st.slider(
    "Budget (€)",
    int(filtered_df["germany_price(euros)"].min()),
    int(filtered_df["germany_price(euros)"].max()),
    60000
)

min_range = st.slider(
    "Minimum Range (km)",
    100,
    int(filtered_df["real_Range(km)"].max()),
    300
)

# ---------------------------------------------------
# Filter results
# ---------------------------------------------------
recommendations = filtered_df[
    (filtered_df["germany_price(euros)"] <= budget) &
    (filtered_df["real_Range(km)"] >= min_range)
].reset_index(drop=True)

display_df = recommendations[[
    "brand_name", "model", "real_Range(km)", "fast_charge(kWh)", "germany_price(euros)"
]].rename(columns={
    "brand_name": "Brand",
    "model": "Model",
    "real_Range(km)": "Range (km)",
    "fast_charge(kWh)": "Fast Charge (kWh)",
    "germany_price(euros)": "Price (€)"
})

# ---------------------------------------------------
# HTML table inside fixed-height scrollable glass card
# ---------------------------------------------------
rows_html = ""
for _, row in display_df.iterrows():
    rows_html += "<tr>"
    for val in row:
        rows_html += f"<td>{val}</td>"
    rows_html += "</tr>"

headers_html = "".join(f"<th>{col}</th>" for col in display_df.columns)

table_html = f"""
<div class="glass">
    <p class="glass-title">Recommended EV Models</p>
    <div class="table-scroll">
        <table class="ev-table">
            <thead><tr>{headers_html}</tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
</div>
"""

st.markdown(table_html, unsafe_allow_html=True)

st.markdown(
    '<p class="footer-text">Built with Python • Pandas • Plotly • Streamlit</p>',
    unsafe_allow_html=True
)