import random
import time

def generate_message():
    """ Generate the message data with random values. """
    return {
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

# Function to produce and send the message, including the sleep to generate a new message every 0.5 seconds
def produce_messages_forever():
    while True:
        # Generate the message
        message = generate_message()
        
        # Here you would insert the code to send the message to Kafka
        # For demonstration, we'll just print the message
        print(message)
        
        # Wait for 0.5 seconds before generating the next message
        #time.sleep(0.05)

# Call the function to start generating messages
produce_messages_forever()
