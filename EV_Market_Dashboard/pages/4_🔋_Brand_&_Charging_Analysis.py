import streamlit as st
import plotly.express as px
from utils.helper import load_data
from utils.styles import local_css

st.set_page_config(page_title="Brand, Market & Charging Analysis", page_icon="🔋", layout="wide")

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

[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 15px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Sidebar Filters ----------
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

# ---------- Title ----------
st.markdown("""
<div style="text-align:center; margin-top:0px; margin-bottom:20px;">
    <span style="
        color: #ffffff;
        font-size: 36px;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.1;
        display: inline-block;
    ">Brand, Market & Charging Analysis</span>
</div>
""", unsafe_allow_html=True)

# Graph 8
brands = (
    filtered_df["brand_name"]
    .value_counts()
    .head(10)
    .reset_index()
)
brands.columns = ["Brand", "Count"]

fig = px.bar(
    brands,
    x="Count",
    y="Brand",
    orientation="h",
    color="Count",
    color_continuous_scale="Viridis",
    template="plotly_dark",
    title="Top 10 EV Brands"
)
fig.update_layout(
    title_x=0.5,
        title_xanchor="center",
    xaxis_title="Number of Models",
    yaxis_title="Brand",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)
fig.update_yaxes(categoryorder="total ascending")
st.plotly_chart(fig, use_container_width=True)

# Graph 9
fig = px.histogram(
    filtered_df,
    x="market_segment",
    color="market_segment",
    template="plotly_dark",
    title="Market Segment Distribution"
)
fig.update_layout(
    title_x=0.5,
        title_xanchor="center",
    showlegend=False,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)

# Graph 10
fig = px.pie(
    filtered_df,
    names="availability",
    hole=0.6,
    template="plotly_dark",
    title="Availability Status"
)
fig.update_layout(
    title_x=0.42,
        title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    margin=dict(r=120)
)
st.plotly_chart(fig, use_container_width=True)

# Graph 11
# Graph 11
fig = px.histogram(
    filtered_df,
    x="germany_price(euros)",
    nbins=30,
    color_discrete_sequence=["#FF7043"],
    template="plotly_dark",
    title="Price Distribution"
)

fig.update_layout(
    title_x=0.5,
    title_xanchor="center",
    xaxis_title="Price (€)",
    yaxis_title="Count",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

# Format x-axis ticks as €25k, €50k, etc.
fig.update_xaxes(
    tickprefix="€",
    tickformat="~s"
)

st.plotly_chart(fig, use_container_width=True)

# Graph 12
fig = px.box(
    filtered_df,
    x="market_segment",
    y="fast_charge(kWh)",
    color="market_segment",
    template="plotly_dark",
    title="Charging Speed by Segment"
)
fig.update_layout(
    title_x=0.5,
        title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)

# Graph 13
# Graph 13
fig = px.scatter(
    filtered_df,
    x="germany_price(euros)",
    y="real_Range(km)",
    color="market_segment",
    hover_name="model",
    template="plotly_dark",
    title="Price vs Range"
)

fig.update_traces(
    marker=dict(size=10, opacity=0.8)
)

fig.update_layout(
    title_x=0.5,
    title_xanchor="center",
    xaxis_title="Price (€)",
    yaxis_title="Range (km)",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

# Format x-axis ticks as €25k, €50k, etc.
fig.update_xaxes(
    tickprefix="€",
    tickformat="~s"
)

st.plotly_chart(fig, use_container_width=True)
# Graph 14
fig = px.pie(
    filtered_df,
    names="drive_type",
    hole=0.5,
    template="plotly_dark",
    title="Drive Type Distribution"
)
fig.update_layout(
    title_x=0.42,
        title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    margin=dict(r=120)
)
st.plotly_chart(fig, use_container_width=True)

# Graph 15
fig = px.histogram(
    filtered_df,
    x="safety_rating",
    color_discrete_sequence=["#66BB6A"],
    template="plotly_dark",
    title="Safety Rating Distribution"
)
fig.update_layout(
    title_x=0.5,
        title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)