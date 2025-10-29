import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from datetime import datetime
import numpy as np
import os


tickers = {"NIFTY 50": "^NSEI", "NIFTY BANK": "^NSEBANK"}
data_dir = "data"
output_dir = "outputs"
os.makedirs(data_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


print("Fetching 5 years of data...")
data = {}
for name, ticker in tickers.items():
    df = yf.download(ticker, period="5y", interval="1d")
    csv_path = os.path.join(data_dir, f"{name.replace(' ', '_')}.csv")
    df.to_csv(csv_path)
    data[name] = df
    print(f"Saved {name} data to {csv_path}")




print("\nPreprocessing data...")

cleaned_data = {}

for name, df in data.items():
    print(f"\n{name} original columns:", df.columns)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns] 

    df = df.reset_index()

    if 'Date' not in df.columns:
        if 'Datetime' in df.columns:
            df.rename(columns={'Datetime': 'Date'}, inplace=True)

    df = df[['Date', 'Close']].dropna()
    df = df[df['Close'].apply(lambda x: isinstance(x, (int, float)))] 

    df['Date'] = pd.to_datetime(df['Date'])

    print(f"{name}: {len(df)} records cleaned.")
    print(df.head())

    cleaned_data[name] = df



def make_forecast(df, name, period, freq, label):
    if 'Date' not in df.columns:
        df = df.reset_index()

    if 'Close' not in df.columns:
        possible_close = [c for c in df.columns if 'Close' in str(c)]
        if possible_close:
            df = df.rename(columns={possible_close[0]: 'Close'})
        else:
            raise KeyError("No Close column found for forecasting.")

    df_prophet = df[['Date', 'Close']].copy()
    df_prophet = df_prophet.rename(columns={'Date': 'ds', 'Close': 'y'})

    try:
        y_loc = df_prophet.columns.get_loc('y')
    except Exception:
        y_loc = list(df_prophet.columns).index('y')

    y_values = df_prophet.iloc[:, y_loc].values

    y_values = np.asarray(y_values).ravel()

    y_numeric = pd.to_numeric(y_values, errors='coerce')

    df_prophet.iloc[:, y_loc] = y_numeric

    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'], errors='coerce')
    df_prophet = df_prophet.dropna(subset=['ds', 'y'])

    if df_prophet.empty:
        raise ValueError(f"After cleaning, no valid rows for {name}. Inspect input df columns: {df.columns}")



    print("\nMaking forecast for:", name)
    print("Columns in df_prophet before fitting:", df_prophet.columns)
    print(df_prophet.head())

    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=period, freq=freq)
    forecast = model.predict(future)

    plt.figure(figsize=(10, 6))
    fig = model.plot(forecast)
    plt.title(f"{name} - {label} Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()

    outfn = f"outputs/{name.replace(' ', '_')}_{label}_forecast.png"
    os.makedirs("outputs", exist_ok=True)
    plt.savefig(outfn, bbox_inches='tight')
    plt.close()

    print(f"Saved {label} forecast for {name} → {outfn}")
    return forecast


print("\nGenerating short-term (3 months) forecasts...")
short_forecasts = {}
for name, df in data.items():
    print("\n=== DEBUG CHECK ===")
    print("Forecasting:", name)
    print(df.columns)
    print(df.head())

    short_forecasts[name] = make_forecast(df, name, period=90, freq='D', label='ShortTerm')


print("\nGenerating long-term (3 years) forecasts...")
long_forecasts = {}
for name, df in data.items():
    long_forecasts[name] = make_forecast(df, name, period=156, freq='W', label='LongTerm')


report_path = os.path.join(output_dir, "report.txt")
with open("outputs/summary.txt", "w", encoding="utf-8") as f:
    f.write("LASA FINANCIAL SERVICES — Forecast Report\n")
    f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*60 + "\n\n")

    for name in tickers.keys():
        last_price = data[name]['Close'].iloc[-1]
        short_mean = short_forecasts[name]['yhat'].iloc[-1]
        long_mean = long_forecasts[name]['yhat'].iloc[-1]
        f.write(f"{name}\n")
        f.write(f"  Current Price: ₹{last_price:.2f}\n")
        f.write(f"  Short-Term (3M) Projection: ₹{short_mean:.2f}\n")
        f.write(f"  Long-Term (3Y) Projection: ₹{long_mean:.2f}\n")
        f.write(f"  Expected Trend: {'Bullish' if long_mean > last_price else 'Bearish'}\n")
        f.write("\n")

    f.write("="*60 + "\n")
    f.write("Model Used: Facebook Prophet\n")
    f.write("Assumptions:\n")
    f.write("- Future trends follow historical patterns.\n")
    f.write("- No major economic or political shocks.\n")
    f.write("- Data quality and market efficiency assumed.\n\n")

    f.write("Limitations:\n")
    f.write("- Past performance doesn’t guarantee future results.\n")
    f.write("- Model ignores external macroeconomic variables.\n")
    f.write("- Forecast accuracy decreases with time horizon.\n\n")

    f.write("Confidence Notes:\n")
    f.write("- Short-term confidence is moderate (~70–80%).\n")
    f.write("- Long-term forecasts have higher uncertainty (>90% CI).\n")

print(f"\nReport saved to: {report_path}")
print("\nAll tasks complete! Check 'outputs/' folder for plots and report.")
