import streamlit as st
import plotly.express as px
from utils.helper import load_data
from utils.styles import local_css


local_css()
st.set_page_config(
    page_title="Advanced Insights & Correlations",
    layout="wide"
)

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

/* Plotly chart card */
[data-testid="stPlotlyChart"]{
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



# Apply filters 
filtered_df = df.copy()

if selected_segments:
    filtered_df = filtered_df[filtered_df["market_segment"].isin(selected_segments)]

if selected_drive:
    filtered_df = filtered_df[filtered_df["drive_type"].isin(selected_drive)]

if selected_brands:
    filtered_df = filtered_df[filtered_df["brand_name"].isin(selected_brands)]


st.markdown("""
<div style="text-align:center; margin-top:0px; margin-bottom:20px;">
    <span style="
        color: #ffffff;
        font-size: 36px;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.1;
        display: inline-block;
    ">Advanced Insights & Correlations</span>
</div>
""", unsafe_allow_html=True)


numeric_cols = [
    "real_Range(km)",
    "efficiency(Wh/km)",
    "fast_charge(kWh)",
    "weight(kg)",
    "acceleration(sec)"
]

corr = filtered_df[numeric_cols].corr()

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="YlGnBu",
    template="plotly_dark",
    title="Correlation Heatmap",
    aspect="auto"
)

fig.update_layout(
    title_x=0.5,
    title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)


fig = px.box(
    filtered_df,
    x="market_segment",
    y="real_Range(km)",
    color="market_segment",
    template="plotly_dark",
    title="Range by Market Segment"
)

fig.update_layout(
    title_x=0.5,
    title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)


fig = px.scatter(
    filtered_df,
    x="fast_charge(kWh)",
    y="real_Range(km)",
    color="market_segment",
    hover_name="model",
    template="plotly_dark",
    title="Battery Capacity vs Range"
)

fig.update_traces(marker=dict(size=10))

fig.update_layout(
    title_x=0.5,
    title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)


fig = px.box(
    filtered_df,
    x="drive_type",
    y="efficiency(Wh/km)",
    color="drive_type",
    template="plotly_dark",
    title="Efficiency by Drive Type"
)

fig.update_layout(
    title_x=0.5,
    title_xanchor="center",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)