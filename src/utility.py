import yfinance as yf

def growth_rate_estimator(ticker, period):
    try:
        # Fetch historical data for the stock
        stock = yf.Ticker(ticker)
        history = stock.history(period=period)  # Adjust the period as needed

        # Calculate annualized growth rate (CAGR)
        initial_price = history["Close"].iloc[0]
        final_price = history["Close"].iloc[-1]
        num_years = len(history) / 252  # Assuming 252 trading days per year
        cagr = (final_price / initial_price) ** (1 / num_years) - 1

        return cagr
    except Exception as e:
        return f"Error estimating growth rate for {ticker}: {str(e)}"
    
def get_stock_price(ticker):
    try:
        # Fetch stock data using yfinance
        stock = yf.Ticker(ticker)
        stock_history = stock.history(period="1d")  # Fetch historical data for 1 day

        # Extract the current stock price
        stock_price = stock_history["Close"].iloc[0]

        return stock_price
    except Exception as e:
        return f"Error fetching stock price for {ticker}: {str(e)}"
    
def get_sector_and_financials(ticker):
    try:
        # Fetch stock data using yfinance
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        # time.sleep(0.02)
        stock_financials = stock.financials

        # Extract sector, market cap, and net earnings
        sector = stock_info.get("sector")
        market_cap = stock_info.get("marketCap")
        net_earnings = stock_financials.loc["Net Income"].iloc[0]

        return sector, market_cap, net_earnings
    except Exception as e:
        return f"Error fetching data for {ticker}: {str(e)}"

def calculate_total_market_cap_and_earnings(tickers):
    total_market_cap = 0
    total_earnings = 0
    for t in tickers:
        _, market_cap, net_earnings = get_sector_and_financials(t)
        if isinstance(market_cap, int) and isinstance(net_earnings, int):
            total_market_cap += market_cap
            total_earnings += net_earnings
    return total_market_cap, total_earnings

def calculate_market_pe_ratio(market_cap, net_earnings):
    try:
        market_pe_ratio = market_cap / net_earnings
        return market_pe_ratio
    except ZeroDivisionError:
        return "Error: Total net earnings are zero."