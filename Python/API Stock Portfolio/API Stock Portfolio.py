import requests
import pandas as pd

# Constants
ALPHA_VANTAGE_API_KEY = 'MY_ALPHA_VANTAGE_API_KEY'  # I would add in my Alpha Vatnage API key here
ALPHA_VANTAGE_BASE_URL = 'https://www.alphavantage.co/query'

# Function to fetch stock data from Alpha Vantage
def fetch_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()

    # Parse the JSON data into a DataFrame
    time_series = data['Time Series (Daily)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.rename(columns={
        '1. open': 'Open', 
        '2. high': 'High', 
        '3. low': 'Low', 
        '4. close': 'Close', 
        '5. volume': 'Volume'
    })
    df.index = pd.to_datetime(df.index)
    return df

# Function to calculate tax lots
def calculate_fifo_tax_lots(purchases, sales):
    remaining_purchases = purchases.copy()
    capital_gains = 0

    for sale in sales:
        sale_shares, sale_price = sale
        while sale_shares > 0 and remaining_purchases:
            purchase_shares, purchase_price = remaining_purchases[0]

            shares_sold = min(sale_shares, purchase_shares)
            sale_shares -= shares_sold
            remaining_purchases[0] = (purchase_shares - shares_sold, purchase_price)

            if remaining_purchases[0][0] == 0:
                remaining_purchases.pop(0)

            gain = (sale_price - purchase_price) * shares_sold
            capital_gains += gain

    return capital_gains

purchases = [(100, 50), (50, 55)]  # (shares, price_per_share)
sales = [(80, 60), (30, 65)]  # (shares, price_per_share)

capital_gains = calculate_fifo_tax_lots(purchases, sales)
print(f"Calculated Capital Gains: ${capital_gains}")


# Function to track price targets and calculate implied upside
def track_price_targets(current_price, target_price):
    implied_upside = ((target_price - current_price) / current_price) * 100
    return implied_upside


symbol = 'AAPL'  # Example stock symbol
stock_data = fetch_stock_data(symbol)

# Assuming the latest data is the current price
current_price = float(stock_data.iloc[0]['Close'])
target_price = 150  # Example target price

implied_upside = track_price_targets(current_price, target_price)
print(f"Implied Upside for {symbol}: {implied_upside}%")
