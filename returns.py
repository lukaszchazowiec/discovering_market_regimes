import numpy as np
import pandas as pd


def load_log_returns(filepath):
    df = pd.read_csv(filepath, header=[0, 1], index_col=0, parse_dates=True)
    returns = np.log(df['Close'] / df['Close'].shift(1)).dropna()
    return returns