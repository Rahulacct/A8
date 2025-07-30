# 📈 NSE Stock Price Forecast App

A simple **Streamlit** app that forecasts the **next 10 trading days** closing prices for **NSE-listed stocks** using **Exponential Smoothing** (Holt-Winters method) from the `statsmodels` library. This app allows you to visualize both historical and predicted stock prices.

---

## 🔧 Features

- **Supports any valid NSE ticker** (e.g., `TCS.NS`, `INFY.NS`, `RELIANCE.NS`)
- **Fetches the last 6 months of historical data** using `yfinance`
- **Forecasts the next 10 trading days** closing prices using **Exponential Smoothing** (Holt-Winters method)
- **Visualizes historical and forecasted prices** with **Matplotlib**
- Easy-to-use **Streamlit interface**

## 📦 Requirements

To run the app locally, you will need to install the following Python packages:

- `streamlit`: For building the web app.
- `yfinance`: To fetch historical stock data from Yahoo Finance.
- `statsmodels`: For applying **Exponential Smoothing**.
- `pandas`: For data manipulation.
- `matplotlib`: For plotting the historical and forecasted stock prices.
```bash
pip install -r requirements.txt
