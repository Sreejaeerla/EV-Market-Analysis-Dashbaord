import streamlit as st
from utils.styles import local_css

# pages/2_📖_About_Project.py

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

    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }

    .pill {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.28);
        color: #ffffff;
        font-size: 14px;
        font-weight: 500;
        padding: 6px 18px;
        border-radius: 30px;
    }

    .avatar {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: rgba(0,230,118,0.12);
        border: 1.5px solid rgba(0,230,118,0.35);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: 700;
        color: #00E676 !important;
        margin-bottom: 12px;
        text-decoration: none;
        transition: all 0.2s ease;
    }

    .avatar:hover {
        background: rgba(0,230,118,0.25);
        border-color: rgba(0,230,118,0.7);
        cursor: pointer;
        transform: scale(1.08);
    }

    .dev-name {
        color: #ffffff;
        font-size: 19px;
        font-weight: 700;
        margin: 0 0 2px;
    }

    .dev-role {
        color: rgba(255,255,255,0.5);
        font-size: 14px;
        margin: 0 0 14px;
    }

    .dev-link {
        color: #00E676;
        font-size: 15px;
        line-height: 2.2;
        text-decoration: none;
        display: block;
    }

    .dev-link:hover { text-decoration: underline; }

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
        ">About Project</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="glass">
        <h2>Project Goal</h2>
        <p>
            The European EV market has grown rapidly, giving consumers a broad and increasingly
            complex range of vehicles to evaluate, while manufacturers must keep pace with shifting
            market dynamics and customer preferences. This dashboard examines the EV landscape —
            vehicle offerings, brand presence, feature availability, and market distribution — to
            help both consumers and manufacturers better understand what's shaping the European
            EV industry.
        </p>
    </div>

    <div class="glass">
        <h2>Key Objectives</h2>
        <div class="obj"><span class="tick">✔</span><span>Explore trends and patterns across the European EV market</span></div>
        <div class="obj"><span class="tick">✔</span><span>Analyze vehicle range and energy efficiency</span></div>
        <div class="obj"><span class="tick">✔</span><span>Compare manufacturers, brand presence, and market segments</span></div>
        <div class="obj"><span class="tick">✔</span><span>Study charging performance and pricing across vehicles</span></div>
        <div class="obj"><span class="tick">✔</span><span>Understand safety and consumer-oriented features</span></div>
        <div class="obj"><span class="tick">✔</span><span>Build an interactive recommendation system</span></div>
    </div>

    <div class="glass">
        <h2>Tech Stack</h2>
        <div class="pill-row">
            <span class="pill">Python</span>
            <span class="pill">Pandas</span>
            <span class="pill">Plotly</span>
            <span class="pill">Streamlit</span>
            <span class="pill">Seaborn</span>
            <span class="pill">Matplotlib</span>
        </div>
    </div>

    <div class="glass">
        <h2>Developed By</h2>
        <a class="avatar" href="https://www.linkedin.com/in/sreeja-eerla-72a53333a" target="_blank">SE</a>
        <p class="dev-name">Sreeja Eerla</p>
        <p class="dev-role">Data Analyst</p>
        <a class="dev-link" href="mailto:eerlasreeja97@gmail.com">📧 &nbsp;eerlasreeja97@gmail.com</a>
        <a class="dev-link" href="https://www.linkedin.com/in/sreeja-eerla-72a53333a" target="_blank">🔗 &nbsp;linkedin.com/in/sreeja-eerla-72a53333a</a>
        <a class="dev-link" href="https://github.com/Sreejaeerla" target="_blank">💻 &nbsp;github.com/Sreejaeerla</a>
    </div>

    <p class="footer-text">Built with Python • Pandas • Plotly • Streamlit</p>
    """,
    unsafe_allow_html=True,
)