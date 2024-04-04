import yfinance as yf
# from utility import 

def pe_ratio_estimator(ticker, growth_rate):
    try:
        # Get stock data
        stock = yf.Ticker(ticker)
        eps = stock.info['trailingEps']
        pe_ratio = stock.info['trailingPE']

        # Calculate intrinsic value
        intrinsic_value = eps * (1 + growth_rate) ** 5 * pe_ratio

        # Discount to present value (using 10% discount rate)
        discount_rate = 0.10
        present_value = intrinsic_value / (1 + discount_rate) ** 5

        return present_value
    except Exception as e:
        return f"Error: {str(e)}"
    
def dcf_estimator(ticker):
    try:
        # Get stock data
        stock = yf.Ticker(ticker)
        eps = stock.info['trailingEps']
        pe_ratio = stock.info['trailingPE']

        # Calculate historical CAGR (3-year period)
        historical_eps = [10, 12, 14]  # Example EPS data for years 1, 2, and 3
        num_years = len(historical_eps)
        cagr = ((historical_eps[-1] / historical_eps[0]) ** (1 / num_years)) - 1

        # Calculate intrinsic value
        expected_growth_rate = cagr
        intrinsic_value = eps * (1 + expected_growth_rate) ** 5 * pe_ratio

        # Discount to present value (using 10% discount rate)
        discount_rate = 0.10
        present_value = intrinsic_value / (1 + discount_rate) ** 5

        return present_value
    except Exception as e:
        return f"Error: {str(e)}"
    
def pe_relative_estimator(ticker, market_pe_ratio):
    try:
        # Get stock data
        stock = yf.Ticker(ticker)
        eps = stock.info['trailingEps']

        # Calculate intrinsic value using P/E Relative approach
        intrinsic_value = eps * market_pe_ratio

        return intrinsic_value
    except Exception as e:
        return f"Error: {str(e)}"