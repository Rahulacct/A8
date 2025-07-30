import streamlit as st
from forecast import forecast_stock  # Import the forecasting function
from utils import plot_forecast  # Import the plotting function

# App title and description
st.title("📈 NSE Stock Price Forecast App")
st.write("Forecasts the **next 10 trading days** closing price using **Exponential Smoothing**.")

# Input for the stock ticker
ticker = st.text_input("Enter NSE Ticker (e.g., TCS.NS, INFY.NS, RELIANCE.NS):", value="INFY.NS")

# Forecast button
if st.button("Forecast"):
    try:
        # Forecast for the given ticker, with the forecast period set to 10 days
        df, forecast_df = forecast_stock(ticker, forecast_days=10)  # Forecasting for 10 days
        
        st.write("### Forecasted Closing Prices for Next 10 Trading Days:")
        st.dataframe(forecast_df)  # Display the forecasted data
        
        # Plot the forecast
        st.pyplot(plot_forecast(df, forecast_df))
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
