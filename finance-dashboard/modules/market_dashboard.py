import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

def dashboard():
    st.title("📈 Stock Market Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        symbol = st.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL").upper()
    with col2:
        start_date = st.date_input("Start Date", datetime(2020, 1, 1))
    with col3:
        end_date = st.date_input("End Date", datetime.today())

    if start_date > end_date:
        st.error("Error: Start date cannot be after End date")
        return

    try:
        with st.spinner('Fetching stock data...'):
            stock_data = yf.download(symbol, start=start_date, end=end_date + pd.DateOffset(1), progress=False)

        if not stock_data.empty:
            st.subheader(f"📊 {symbol} Stock Performance")
            st.line_chart(stock_data['Close'])

            st.subheader("Recent Data")
            st.dataframe(stock_data.tail(10))

        else:
            st.warning("No data found for the given stock symbol and date range")

    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
