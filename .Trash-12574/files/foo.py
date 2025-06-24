import streamlit as st
from st_pages import Page, show_pages, add_page_title

# 1) Configure your layout
st.set_page_config(layout="wide")

# 2) Tell st_pages exactly which files to show (and give each an emoji)
show_pages([
    Page("apps/home_page.py",           "Home",               "🏠"),
    Page("apps/rate_curves_page.py",   "Rate Curves",        "📈"),
    Page("apps/rate_curve_surface.py", "Rate Curve Surface", "📊"),
    Page("apps/rate_simulations_page.py","Rate Simulations",  "🔄"),
    Page("apps/treasury_inventory.py", "Treasury Inventory", "💼"),
    Page("apps/treasury_risk.py",      "Treasury Risk",      "⚠️"),
    Page("apps/interest_rate_page.py", "Overnight Rates",    "⏰"),
])

# 3) Automatically add the current page’s title + icon at the top
add_page_title()
