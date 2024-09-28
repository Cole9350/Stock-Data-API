# Stock Data Service API

A Flask-based API service that fetches stock market data from Alpha Vantage and caches it using Redis.

## Features
- Fetch real-time stock data.
- Retrieve historical stock data.
- Search for stock symbols by keyword.

## Endpoints

### 1. `/stock/<symbol>`
- **Description**: Fetches real-time stock data for a given symbol.
- **Method**: GET
- **Response**:
    ```json
    {
      "symbol": "AAPL",
      "price": 150.25,
      "volume": 1200000,
      "timestamp": "2024-09-27T12:00:00Z"
    }
    ```

### 2. `/stock/<symbol>/history`
- **Description**: Fetches historical stock data for the given symbol.
- **Method**: GET
- **Response**: JSON with historical stock prices.

### 3. `/stock/search/<keyword>`
- **Description**: Searches for stock symbols based on a keyword.
- **Method**: GET
- **Response**: JSON with potential stock symbol matches.

## Setup Instructions

### Prerequisites
- **Python 3.9+**
- **Docker and Docker Compose**
- **Alpha Vantage API Key**

### Steps to Run Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/stock-data-service.git
    cd stock-data-service
    ```

2. **Create a `.env` File**:
    In the project’s root directory, create a `.env` file and add your Alpha Vantage API key:
    ```bash
    ALPHA_VANTAGE_API_KEY=your_real_api_key_here
    ```

3. **Install Dependencies**:
    Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Docker Containers**:
    Make sure you have Docker and Docker Compose installed. To run the application in Docker:
    ```bash
    docker-compose up --build
    ```

5. **Access the API**:
    The API will be running on `http://localhost:5001`. You can use `curl` or Postman to make requests.

### Example Request
To fetch real-time stock data for Apple:
```bash
curl http://localhost:5001/stock/AAPL

## Postman Collection

To test the Stock Data Service API using Postman:

1. Download the [Postman Collection](./postman_collection.json).
2. Open Postman and click `File -> Import`.
3. Select the downloaded `.json` file to import the collection.
4. Run the predefined requests to test the API.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

