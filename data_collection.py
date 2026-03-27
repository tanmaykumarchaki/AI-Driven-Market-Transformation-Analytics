import os
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
import datetime

# ==============================
# 1. Create Data Directory
# ==============================

os.makedirs("data", exist_ok=True)

# ==============================
# 2. Define Time Range
# ==============================

start = "2010-01-01"
end = "2025-01-01"

# ==============================
# 3. STOCK MARKET DATA
# ==============================

stocks = {
    "NIFTY50": "^NSEI",
    "SENSEX": "^BSESN",
    "S&P500": "^GSPC",
    "APPLE": "AAPL",
    "TESLA": "TSLA"
}

for name, ticker in stocks.items():
    print(f"Downloading {name}...")
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(f"data/{name}.csv")

# ==============================
# 4. ADD RETURNS & VOLATILITY
# ==============================

def add_features(file):
    df = pd.read_csv(file)

    # Ensure Date column exists and is parsed
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Convert Close column to numeric (CRITICAL FIX)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    # Drop rows where Close is NaN
    df = df.dropna(subset=['Close'])

    # Calculate returns (FIXED WARNING ALSO)
    df['returns'] = df['Close'].pct_change(fill_method=None)

    # Volatility
    df['volatility'] = df['returns'].rolling(30).std()

    df.to_csv(file, index=False)

# ==============================
# 5. FRED MACRO DATA
# ==============================

fred_series = {
    "Interest_Rate": "FEDFUNDS",
    "Inflation_CPI": "CPIAUCSL",
    "Unemployment": "UNRATE"
}

for name, code in fred_series.items():
    print(f"Downloading {name} from FRED...")
    df = pdr.get_data_fred(code, start, end)
    df.to_csv(f"data/{name}.csv")

# ==============================
# 6. AI ERA FLAG (IMPORTANT)
# ==============================

def add_ai_flag(file):
    df = pd.read_csv(file)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df['AI_Era'] = df['Date'].apply(lambda x: 0 if x.year < 2020 else 1)
        df.to_csv(file, index=False)

for file in os.listdir("data"):
    if file.endswith(".csv"):
        add_ai_flag(f"data/{file}")

print("✅ Data Collection Completed Successfully!")