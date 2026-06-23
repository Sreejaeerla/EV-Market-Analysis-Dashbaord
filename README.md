#  European EV Market Dashboard

An interactive data analytics dashboard built with **Python** and **Streamlit** that explores the European Electric Vehicle (EV) market — covering vehicle offerings, brand presence, feature availability, pricing, and market distribution.

---

##  Project Overview

The European EV market has grown rapidly, giving consumers a broad and increasingly complex range of vehicles to evaluate, while manufacturers must keep pace with shifting market dynamics and customer preferences. This dashboard examines the EV landscape to help both consumers and manufacturers better understand what's shaping the European EV industry.

---

##  Folder Structure

```
WEB_SCRAPING_EDA/
│
├── .streamlit/
│   └── config.toml          # Streamlit configuration
│
├── 1.data/
│   └── cleaned_EV_Dataset3.xls  # Cleaned EV dataset
│
├── images/
│   ├── e_car.avif
│   └── ev_car.avif
│
├── pages/
│   ├── 2_About_Project.py
│   ├── 3_Dataset_Overview.py
│   ├── 4_Brand_&_Charging_Analysis.py
│   ├── 5_Range_Efficiency_Analysis.py
│   ├── 6_Correlation_Insights.py
│   ├── 7_Recommendation_System.py
│   └── 8_Conclusions.py
│
├── utils/
│   ├── __init__.py
│   ├── helper.py            # Data loading utilities
│   └── styles.py            # Global CSS styling
│
├── Home.py                  # Main entry point
├── requirements.txt         # Python dependencies
└── README.md
```

---

##  Dashboard Pages

| Page | Description |
|------|-------------|
| 🏠 Home | Landing page with project introduction |
| 📖 About Project | Project goals, tech stack, and developer info |
| 📋 Dataset Overview | KPIs, dataset shape, preview, data types, and summary statistics |
| 🔋 Brand & Charging Analysis | Top brands, market segments, pricing, drive types, and safety ratings |
| 📈 Range & Efficiency Analysis | Efficiency, range, weight, acceleration, and charging distributions |
| 🔗 Correlation Insights | Heatmaps and scatter plots exploring feature relationships |
| 🎯 Recommendation System | Filter-based EV recommendation engine |
| 📝 Conclusions | Key insights and recommendations |

---

##  Key Objectives

- ✔ Explore trends and patterns across the European EV market
- ✔ Analyze vehicle range and energy efficiency
- ✔ Compare manufacturers, brand presence, and market segments
- ✔ Study charging performance and pricing across vehicles
- ✔ Understand safety and consumer-oriented features
- ✔ Build an interactive recommendation system

---

##  Key Insights

- Most EV models are concentrated in the **mid-range category**, balancing range, efficiency, and affordability
- **Segment C** is the most competitive market segment with the highest number of models
- Vehicles with **longer ranges and faster charging** tend to be priced higher
- **Energy consumption increases with vehicle weight**
- Advanced features like heat pumps and towing capability are more common in **higher-end vehicles**

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Web dashboard framework |
| Pandas | Data manipulation |
| Plotly | Interactive charts |
| Seaborn | Statistical visualizations |
| Matplotlib | Supporting visualizations |

---


##  Requirements

```
streamlit
pandas
plotly
seaborn
matplotlib
openpyxl
```

---



*Built with Python • Pandas • Plotly • Streamlit*
