import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load historical stock data into a Pandas dataframe
df = pd.read_csv('new.csv')

# Check for the presence of the required column names
required_columns = ['Date', 'Close']
if not set(required_columns).issubset(set(df.columns)):
    print("Error: Required columns not found in the data frame. Required columns: ", required_columns)
    exit()

# Calculate the moving average of the stock price over a given window
def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

# Calculate the exponential moving average of the stock price over a given window
def exponential_moving_average(data, window):
    return data['Close'].ewm(span=window).mean()

# Plot the stock price and the moving average
def plot_stock_data(data, window):
    # Calculate the moving average
    moving_average = data['Close'].rolling(window=window).mean()

    # Plot the stock price and the moving average
    plt.plot(data['Date'], data['Close'], label='Stock Price')
    plt.plot(data['Date'], moving_average, label='Moving Average')
    plt.legend()
    plt.show()

# Plot the stock price and the exponential moving average
def plot_exponential_moving_average(data, window):
    # Calculate the exponential moving average
    exponential_moving_average = data['Close'].ewm(span=window).mean()

    # Plot the stock price and the exponential moving average
    plt.plot(data['Date'], data['Close'], label='Stock Price')
    plt.plot(data['Date'], exponential_moving_average, label='Exponential Moving Average')
    plt.legend()
    plt.show()

# Predict the trend direction based on the moving average
def predict_trend_direction(data, window):
    moving_average = data['Close'].rolling(window=window).mean()
    current_price = data['Close'][-1]
    trend_direction = None

    if current_price > moving_average[-1]:
        trend_direction = 'Up'
    else:
        trend_direction = 'Down'

    return trend_direction

# Predict the trend direction based on the exponential moving average
def predict_exponential_trend_direction(data, window):
    exponential_moving_average = data['Close'].ewm(span=window).mean()
    current_price = data['Close'][-1]
    trend_direction = None

    if current_price > exponential_moving_average[-1]:
        trend_direction = 'Up'
    else:
        trend_direction = 'Down'

    return trend_direction

# Plot the stock price and moving average
plot_stock_data(df, 50)

# Plot the stock price and exponential moving average
plot_exponential_moving_average(df, 50)

# Predict the trend direction based
# Load historical stock data into a Pandas dataframe
df = pd.read_csv('new.csv')

# Check for the column names in the data frame
if set(['Date', 'Close']).issubset(set(df.columns)):
    # Plot the stock price and moving average
    plot_stock_data(df, 50)

    # Plot the stock price and exponential moving average
    plot_exponential_moving_average(df, 50)

    # Predict the trend direction based on the moving average
    trend_direction = predict_trend_direction(df, 50)
    print(f'The trend direction is: {trend_direction}')

    # Predict the trend direction based on the exponential moving average
    exponential_trend_direction = predict_exponential_trend_direction(df, 50)
    print(f'The exponential trend direction is: {exponential_trend_direction}')
else:
    print('The data frame does not contain the required column names.')
