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
    font-size: 16px;
    font-weight: 700;
    margin: 0 0 14px 0;
}

/* KPI row — stretches full width, evenly spaced with dividers */
.kpi-row {
    display: flex;
    flex-wrap: nowrap;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
}

.kpi-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
    padding: 0 28px;
    border-right: 1px solid rgba(255,255,255,0.10);
}

.kpi-item:first-child { padding-left: 0; }
.kpi-item:last-child  { padding-right: 0; border-right: none; }

.kpi-label {
    color: #ffffff;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
}

.kpi-value {
    color: #ffffff;
    font-size: 34px;
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.5px;
}

/* Scrollable table wrapper */
.table-scroll {
    height: 360px;
    overflow-y: auto;
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.08);
}

.table-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
.table-scroll::-webkit-scrollbar-track { background: rgba(255,255,255,0.04); border-radius: 4px; }
.table-scroll::-webkit-scrollbar-thumb { background: rgba(0,230,118,0.35); border-radius: 4px; }

.ev-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

.ev-table thead tr th {
    position: sticky;
    top: 0;
    z-index: 2;
    background-color: #1e3a2e !important;
    color: #ffffff !important;
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
    color: #ffffff;
    padding: 7px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    font-size: 13px;
    white-space: nowrap;
}

.ev-table tbody tr:hover td {
    background-color: #1e3d2c;
}

/* column name pills */
.col-pill {
    display: inline-block;
    background: rgba(0,230,118,0.08);
    border: 1px solid rgba(0,230,118,0.28);
    color: #ffffff;
    font-size: 13px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 30px;
    margin: 4px 4px 4px 0;
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
    ">Dataset Overview</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# KPIs — full-width inside one glass card
# ---------------------------------------------------
kpi_df = filtered_df if not filtered_df.empty else df
avg_price = kpi_df["germany_price(euros)"].mean()
avg_range = kpi_df["real_Range(km)"].mean()

st.markdown(f"""
<div class="glass">
    <div class="kpi-row">
        <div class="kpi-item">
            <span class="kpi-label">Total Models</span>
            <span class="kpi-value">{kpi_df['model'].nunique():,}</span>
        </div>
        <div class="kpi-item">
            <span class="kpi-label">Brands</span>
            <span class="kpi-value">{kpi_df['brand_name'].nunique()}</span>
        </div>
        <div class="kpi-item">
            <span class="kpi-label">Avg. Price</span>
            <span class="kpi-value">€{avg_price:,.0f}</span>
        </div>
        <div class="kpi-item">
            <span class="kpi-label">Avg. Range</span>
            <span class="kpi-value">{avg_range:,.0f} km</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Dataset Shape
# ---------------------------------------------------
rows, cols = filtered_df.shape
st.markdown(f"""
<div class="glass">
    <p class="glass-title">Dataset Shape</p>
    <p style="color:#ffffff; font-size:20px; margin:0; font-weight:600;">
        <span style="font-weight:800;">{rows}</span> rows &nbsp;×&nbsp;
        <span style="font-weight:800;">{cols}</span> columns
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Columns + Preview in one card
# ---------------------------------------------------
preview_df = filtered_df.head(10)
headers_html = "".join(f"<th>{col}</th>" for col in preview_df.columns)
rows_html = "".join(
    "<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>"
    for _, row in preview_df.iterrows()
)

# Build columns table rows
col_rows = "".join(
    f"<tr><td>{i}</td><td>{c}</td></tr>"
    for i, c in enumerate(filtered_df.columns)
)

st.markdown(f"""
<div class="glass">
    <p class="glass-title">Columns</p>
    <div class="table-scroll" style="height:260px;">
        <table class="ev-table">
            <thead><tr><th>Index</th><th>Column Name</th></tr></thead>
            <tbody>{col_rows}</tbody>
        </table>
    </div>
</div>
<div class="glass">
    <p class="glass-title">Preview</p>
    <div class="table-scroll">
        <table class="ev-table">
            <thead><tr>{headers_html}</tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Data Types
# ---------------------------------------------------
dtype_rows = "".join(
    f"<tr><td>{col}</td><td>{str(dtype)}</td></tr>"
    for col, dtype in filtered_df.dtypes.items()
)
st.markdown(f"""
<div class="glass">
    <p class="glass-title">Data Types</p>
    <div class="table-scroll" style="height:260px;">
        <table class="ev-table">
            <thead><tr><th>Column</th><th>Type</th></tr></thead>
            <tbody>{dtype_rows}</tbody>
        </table>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Summary Statistics
# ---------------------------------------------------
desc_df = filtered_df.describe().round(2)
desc_headers = "".join(f"<th>{col}</th>" for col in ["Stat"] + list(desc_df.columns))
desc_rows = "".join(
    "<tr><td><strong>" + str(stat) + "</strong></td>" +
    "".join(f"<td>{v}</td>" for v in row) + "</tr>"
    for stat, row in desc_df.iterrows()
)

st.markdown(f"""
<div class="glass">
    <p class="glass-title">Summary Statistics</p>
    <div class="table-scroll" style="height:300px;">
        <table class="ev-table">
            <thead><tr>{desc_headers}</tr></thead>
            <tbody>{desc_rows}</tbody>
        </table>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="footer-text">Built with Python • Pandas • Plotly • Streamlit</p>',
    unsafe_allow_html=True
)