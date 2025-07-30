import matplotlib.pyplot as plt

def plot_forecast(df, forecast_df, currency="INR"):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot historical data (closing prices)
    df['Close'].plot(ax=ax, label="Historical", color='blue')

    # Plot forecasted data (forecasted closing prices)
    forecast_df['Forecast'].plot(ax=ax, label="Forecast", color='red', linestyle='--')

    # Set title and labels
    ax.set_title(f"Stock Price Forecast (Next {len(forecast_df)} Trading Days)")
    ax.set_ylabel(f"Price ({currency})")
    ax.set_xlabel("Date")
    
    # Add legend to differentiate historical data and forecasted data
    ax.legend()

    return fig
