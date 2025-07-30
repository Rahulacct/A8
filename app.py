import streamlit as st
from forecast import forecast_stock  # Import the forecasting function from forecast.py
from plot_forecast import plot_forecast  # Import the plotting function from plot_forecast.py

st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #1E3D58;
        }
        .header {
            font-size: 24px;
            font-weight: 600;
            color: #0077b6;
        }
        .subheader {
            font-size: 18px;
            font-weight: 500;
            color: #023e8a;
        }
        .description {
            font-size: 16px;
            font-weight: 300;
            color: #3d5a80;
        }
        .forecast-button {
            background-color: #0096c7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 18px;
        }
        .forecast-button:hover {
            background-color: #00b4d8;
        }
        .input-container {
            margin-bottom: 20px;
        }
        .result-container {
            margin-top: 20px;
        }
        .forecast-title {
            font-size: 20px;
            color: #005f73;
        }
        .forecast-box {
            background-color: #e0f7fa;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("<div class='title'>📈 NSE Stock Price Forecast App</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>A simple **Streamlit** app to forecast the **next 10 trading days** closing prices of **NSE-listed stocks** using **Exponential Smoothing**.</div>", unsafe_allow_html=True)

# Layout with columns for the input section and results
col1, col2 = st.columns([2, 1])

# Input for the stock ticker and forecast days
with col1:
    st.markdown("<div class='header'>Enter Stock Ticker</div>", unsafe_allow_html=True)
    ticker = st.text_input("Enter NSE Ticker (e.g., `TCS.NS`, `INFY.NS`, `RELIANCE.NS`):", value="INFY.NS")

    # Slider to choose the number of forecast days
    forecast_days = st.slider("Select the number of forecast days", min_value=5, max_value=30, value=10, step=1)

# Forecast button with custom styling
with col2:
    st.markdown("<div class='header'>Forecasting</div>", unsafe_allow_html=True)
    forecast_button = st.button("Generate Forecast", key="forecast", help="Click to generate forecast", use_container_width=True)

# Display output based on user input
if forecast_button:
    try:
        df, forecast_df = forecast_stock(ticker, forecast_days)

        # Display forecasted data
        st.markdown("<div class='forecast-title'>### Forecasted Closing Prices for Next {} Trading Days:</div>".format(forecast_days), unsafe_allow_html=True)
        st.dataframe(forecast_df)

        # Plot the forecasted data
        fig = plot_forecast(df, forecast_df)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
