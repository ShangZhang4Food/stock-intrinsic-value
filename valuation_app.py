import streamlit as st
import pandas as pd
from src.utility import get_sector_and_financials, get_stock_price, growth_rate_estimator, calculate_market_pe_ratio
from src.estimators import pe_ratio_estimator, dcf_estimator, pe_ratio_estimator

# Streamlit app
def main():
    st.title("Stock Intrinsic Value Calculator")
    st.write("Enter a stock ticker to calculate intrinsic value.")

    # Input fields
    ticker = st.text_input("Enter stock ticker (e.g., AAPL):")
    periods_to_select = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd"]
    period = st.selectbox("Historical period to estimate future growth rate.",periods_to_select)


    # Calculate intrinsic value
    if st.button("Estimate"):

        sector, market_cap, net_earnings = get_sector_and_financials(ticker)
        current_stock_price = get_stock_price(ticker)
        pe_intrinsic_value = pe_ratio_estimator(ticker, growth_rate_estimator(ticker, period))
        dcf_intrinsic_value = dcf_estimator(ticker)
        pe_relative_intrinsic_value = pe_ratio_estimator(ticker, calculate_market_pe_ratio(market_cap, net_earnings))
        
        df = pd.DataFrame({'Stock': [ticker],
                           'Market sector': [sector],
                           'Current price': [current_stock_price],
                           'Value - PE': [pe_intrinsic_value],
                           'Value - DCF': [dcf_intrinsic_value],
                           'Value - PE relative': [pe_relative_intrinsic_value]})
        
        st.dataframe(df)

if __name__ == "__main__":
    main()