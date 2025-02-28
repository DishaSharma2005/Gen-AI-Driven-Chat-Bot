import streamlit as st

def financial_calculators():
    st.title("🧮 Financial Calculators")

    with st.expander("Compound Interest Calculator"):
        principal = st.number_input("Principal Amount", min_value=0, value=1000)
        rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0)
        years = st.number_input("Investment Period (Years)", min_value=1, value=10)
        compound_freq = st.selectbox("Compounding Frequency", ["Annually", "Monthly", "Daily"])

        freq_map = {"Annually": 1, "Monthly": 12, "Daily": 365}
        n = freq_map[compound_freq]

        amount = principal * (1 + (rate / 100) / n) ** (n * years)
        st.subheader(f"Future Value: ${amount:,.2f}")
