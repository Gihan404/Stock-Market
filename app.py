"""
# Imports libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
#from keras.models import load_model
import streamlit as st


# Define the list of 40 stock companies to analyze
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'IBM', 'GOOG', 'BABA', 'NFLX', 'INTC',
                   'CSCO', 'VZ', 'DIS', 'GS', 'JPM', 'BA', 'KO', 'PEP', 'JNJ', 'PG',
                   'WMT', 'HD', 'UNH', 'MMM', 'MCD', 'CAT', 'GE', 'KO', 'XOM', 'CVX',
                   'AAP', 'WFC', 'C', 'MS', 'GS', 'JPM', 'BA', 'INTC', 'AMD', 'NVDA']
                   

st.title('SOLFINTECH')
st.title('Stock Market Price Forecasting Application')

selected_tickers = st.sidebar.multiselect('Select Tickers', tickers)
start_date = st.sidebar.date_input('Start Date')
end_date = '2024-01-05'
st.sidebar.header("user Input")


"""

import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
