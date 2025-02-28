""" Keep only the Streamlit page navigation logic.
Remove the actual feature implementations and import them from separate files."""

import streamlit as st
from modules.market_dashboard import dashboard
from modules.currency import currency_converter
from modules.news import financial_news
from modules.portfolio import portfolio_tracker
from modules.calculators import financial_calculators

# Set page configuration
st.set_page_config(
    page_title="Finance Dashboard",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Currency Converter", "Financial News", "Portfolio Tracker", "Calculators"])

# Routing Pages
if page == "Dashboard":
    dashboard()
elif page == "Currency Converter":
    currency_converter()
elif page == "Financial News":
    financial_news()
elif page == "Portfolio Tracker":
    portfolio_tracker()
elif page == "Calculators":
    financial_calculators()

# Footer
st.markdown("---")
st.markdown("© 2025 Finance Dashboard - Created with Streamlit")
