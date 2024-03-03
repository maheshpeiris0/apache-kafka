import random
import time
from flask import Flask, jsonify
import threading

app = Flask(__name__)

# Global variable to store the latest message
latest_message = {}

def generate_message():
    """Generate and update the global variable with the message data with random values."""
    while True:
        global latest_message
        latest_message = {
            "event_type": "A",
            "symbol": random.choice(["PLUG", "AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "FB", "NVDA", "PYPL", "INTC", "CSCO", "CMCSA", "PEP", "ADBE", "NFLX", "AVGO", "TXN", "COST", "QCOM", "TMUS"]),
            "volume": random.randint(50, 1500),
            "accumulated_volume": random.randint(1000000, 50000000),
            "official_open_price": round(random.uniform(1, 5), 2),
            "vwap": round(random.uniform(1, 5), 2),
            "open": round(random.uniform(1, 10), 2),
            "close": round(random.uniform(1, 10), 2),
            "high": round(random.uniform(1, 12), 2),
            "low": round(random.uniform(1, 8), 2),
            "aggregate_vwap": round(random.uniform(1, 5), 4),
            "average_size": random.randint(50, 150),
            "start_timestamp": int(time.time() * 1000),
            "end_timestamp": int(time.time() * 1000) + 1000,
            "otc": None
        }
        time.sleep(0.01)  # Wait for 0.01 seconds before generating the next message

@app.route('/')
def get_latest_message():
    """Return the latest message as a JSON response."""
    print(latest_message)
    return jsonify(latest_message)

if __name__ == '__main__':
    # Start the background thread to generate messages
    threading.Thread(target=generate_message, daemon=True).start()
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080, threaded=True)
