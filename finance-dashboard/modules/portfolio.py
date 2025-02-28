import streamlit as st
import pandas as pd

def portfolio_tracker():
    st.title("📊 Portfolio Tracker")

    if "portfolio" not in st.session_state:
        st.session_state["portfolio"] = []

    with st.expander("Add New Investment"):
        col1, col2, col3 = st.columns(3)
        with col1:
            symbol = st.text_input("Stock Symbol").upper()
        with col2:
            quantity = st.number_input("Quantity", min_value=0.1, value=1.0, step=0.1)
        with col3:
            price = st.number_input("Buy Price", min_value=0.1, value=100.0, step=1.0)

        if st.button("Add to Portfolio"):
            st.session_state["portfolio"].append({"Symbol": symbol, "Quantity": quantity, "Price": price})
            st.success("Added Successfully!")

    st.subheader("Your Portfolio")
    if st.session_state["portfolio"]:
        df = pd.DataFrame(st.session_state["portfolio"])
        st.dataframe(df)
    else:
        st.info("No investments added yet.")
