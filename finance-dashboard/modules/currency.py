import streamlit as st
import yfinance as yf

def currency_converter():
    st.title("💱 Currency Converter")
    
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'INR']
    
    col1, col2, col3 = st.columns(3)
    with col1:
        from_currency = st.selectbox("From Currency", currencies)
    with col2:
        to_currency = st.selectbox("To Currency", currencies)
    with col3:
        amount = st.number_input("Amount", min_value=0.1, value=1.0, step=0.1)

    if st.button("Convert"):
        try:
            pair = f"{from_currency}{to_currency}=X"
            data = yf.download(pair, period="1d")

            if not data.empty:
                rate = data['Close'][-1]
                result = amount * rate
                st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                st.error("Invalid currency pair")

        except Exception as e:
            st.error(f"Conversion failed: {str(e)}")
