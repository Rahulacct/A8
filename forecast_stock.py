import yfinance as yf
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import timedelta

def forecast_stock(ticker, forecast_days=10):
    # Download the stock data (last 6 months)
    df = yf.download(ticker, period="6mo", interval="1d")
    
    if df.empty:
        raise ValueError(f"No data found for ticker symbol: {ticker}")
    
    # Focus on the 'Close' price and drop any missing values
    df = df[['Close']].dropna()

    # Build and fit the Exponential Smoothing model
    model = ExponentialSmoothing(df['Close'], trend='add', seasonal=None)
    model_fit = model.fit()

    # Forecast the next `forecast_days`
    forecast = model_fit.forecast(forecast_days)

    # Generate forecasted dates (business days only)
    last_date = df.index[-1]
    forecast_dates = pd.bdate_range(start=last_date + timedelta(days=1), periods=forecast_days)

    # Create a DataFrame for the forecasted values
    forecast_df = pd.DataFrame({
        "Date": forecast_dates,
        "Forecast": forecast
    }).set_index("Date")

    return df, forecast_df
