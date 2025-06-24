# apps/dashboard.py
import streamlit as st
import altair as alt
import importlib

# 1) Page config + styling
st.set_page_config(layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@alt.theme.register('domino', enable=True)
def domino_theme():
    return {
        "config": {
            "background": "#FFFFFF",
            "axis": { ... },
            "legend": { ... },
            "title": { ... }
        }
    }

# 2) Define your pages and emojis (just for labels—no validator here)
PAGES = {
    "🏠 Home":              "home_page",
    "📈 Rate Curves":       "rate_curves_page",
    "📊 Rate Curve Surface":"rate_curve_surface",
    "🔄 Simulations":       "rate_simulations_page",
    "💼 Inventory":         "treasury_inventory",
    "⚠️  Risk":             "treasury_risk",
    "⏰ Overnight Rates":   "interest_rate_page",
}

# 3) Sidebar nav
choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
module_name = PAGES[choice]

# 4) Dynamically load & run the selected page
page = importlib.import_module(module_name)
page.app()
