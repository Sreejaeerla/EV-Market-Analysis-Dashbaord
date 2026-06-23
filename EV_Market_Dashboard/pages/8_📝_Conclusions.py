import streamlit as st
from utils.styles import local_css

local_css()

st.markdown(
    """
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

    .glass h2 {
        color: #ffffff;
        font-size: 24px;
        font-weight: 700;
        margin-top: 0;
        margin-bottom: 14px;
    }

    .glass p {
        color: rgba(255, 255, 255, 0.82);
        font-size: 16px;
        line-height: 1.85;
        margin: 0;
    }

    .obj {
        color: rgba(255,255,255,0.82);
        font-size: 16px;
        line-height: 1.85;
        margin: 7px 0;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }

    .tick {
        color: #00E676;
        font-weight: bold;
        flex-shrink: 0;
        margin-top: 2px;
    }

    .check {
        color: #00c853;
        font-weight: bold;
        flex-shrink: 0;
        margin-top: 2px;
    }

    .footer-text {
        color: rgba(255,255,255,0.25);
        font-size: 13px;
        text-align: center;
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align:center; margin-top:0px; margin-bottom:20px;">
        <span style="
            color: #ffffff;
            font-size: 36px;
            font-weight: 800;
            letter-spacing: -1px;
            line-height: 1.1;
            display: inline-block;
        ">Conclusions & Recommendations</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="glass">
        <h2>Key Insights</h2>
        <div class="obj"><span class="tick">✔</span><span>Most EV models are concentrated in the mid-range category, offering a balance between driving range, efficiency, and affordability.</span></div>
        <div class="obj"><span class="tick">✔</span><span>Vehicle segment has a strong impact on pricing, with premium and luxury categories commanding significantly higher prices than compact and mid-sized vehicles.</span></div>
        <div class="obj"><span class="tick">✔</span><span>Segment C is the most competitive market segment, containing the highest number of EV models and manufacturer participation.</span></div>
        <div class="obj"><span class="tick">✔</span><span>Vehicles with longer driving ranges and faster charging capabilities tend to be priced higher, highlighting the value consumers place on convenience and performance.</span></div>
        <div class="obj"><span class="tick">✔</span><span>Energy consumption generally increases with vehicle weight, indicating that heavier vehicles require more power to operate efficiently.</span></div>
        <div class="obj"><span class="tick">✔</span><span>Advanced features such as heat pumps, towing capability, and higher safety ratings are more common in higher-end vehicles, contributing to their market positioning and value.</span></div>
    </div>

    <div class="glass">
        <h2>Recommendations</h2>
        <div class="obj"><span class="check">✅</span><span>Manufacturers should focus on improving efficiency and reducing vehicle weight to enhance range and overall performance.</span></div>
        <div class="obj"><span class="check">✅</span><span>Expand fast-charging capabilities across more vehicle segments to improve convenience and customer satisfaction.</span></div>
        <div class="obj"><span class="check">✅</span><span>Prioritize innovation in highly competitive segments, particularly Segment C, where consumer demand is strongest.</span></div>
        <div class="obj"><span class="check">✅</span><span>Consumers should evaluate EVs based on overall value, considering range, charging capability, efficiency, safety, and price together.</span></div>
        <div class="obj"><span class="check">✅</span><span>Industry stakeholders should continue investing in charging infrastructure to support the growing adoption of electric vehicles.</span></div>
    </div>

    <p class="footer-text">Built with Python • Pandas • Plotly • Streamlit</p>
    """,
    unsafe_allow_html=True,
)