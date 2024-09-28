from flask import Flask, jsonify
import redis
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Connecting to Redis (Redis container is named 'redis')
redis_client = redis.Redis(host='redis', port=6379)

# Alpha Vantage API URL and Key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={key}'

# Fetch stock data from Alpha Vantage and cache in Redis
@app.route('/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    # Check if data is in cache
    cached_data = redis_client.get(symbol)
    
    if cached_data:
        return jsonify(eval(cached_data))  # Return cached data

    # Fetch from Alpha Vantage API
    response = requests.get(BASE_URL.format(symbol=symbol, key=API_KEY))
    
    if response.status_code == 200:
        data = response.json()
        # Cache the result for 60 seconds
        redis_client.set(symbol, str(data), ex=60)
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500
    
@app.route('/stock/search/<keyword>', methods=['GET'])
def search_stock_symbol(keyword):
    try:
        response = requests.get(f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={API_KEY}")
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Failed to search symbol'}), 500
    except Exception as e:
        app.logger.error(f"Error searching for symbol with keyword {keyword}: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
    
@app.route('/stock/<symbol>/history', methods=['GET'])
def get_stock_history(symbol):
    try:
        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}")
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Failed to fetch historical data'}), 500
    except Exception as e:
        app.logger.error(f"Error fetching historical data for {symbol}: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
