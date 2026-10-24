import numpy as np
import pandas as pd

tickers = [
    "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL",  # Big Tech / wzrostowe
    "JPM", "JNJ", "XOM", "PG", "DIS",         # Finanse, Zdrowie, Energetyka, Konsumenckie, Media
    "GLD", "SLV", "USO", "TLT", "VNQ",        # Złoto, Srebro, Ropa (ETF), Obligacje skarbowe US, Nieruchomości (REIT)
]

def load_log_returns(filepath):
    df = pd.read_csv(filepath, header=[0, 1], index_col=0, parse_dates=True)
    returns = np.log(df['Close'] / df['Close'].shift(1)).dropna()
    return returns


ret = load_log_returns("historical_data/market_15_assets_10y.csv")
print(ret.head())