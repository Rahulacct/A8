# 📈 NSE Stock Price Forecast App

A simple **Streamlit** app to forecast the next **10 trading days** closing prices of **NSE-listed stocks** using **Exponential Smoothing** from `statsmodels`.

## 🔧 Features

- Supports any valid **NSE ticker** (e.g., `TCS.NS`, `INFY.NS`, `RELIANCE.NS`)
- Uses `yfinance` to fetch the last **6 months** of historical data
- Forecasts the next **10 trading days** using **Exponential Smoothing** (Holt-Winters method)
- Visualizes historical and forecasted prices using **Matplotlib**
  
## ▶️ How to Run

### 1. **Clone the repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/nse-forecast-app.git
   cd nse-forecast-app
