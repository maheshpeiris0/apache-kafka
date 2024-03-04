from confluent_kafka import Producer
import json
import time
import random


# Define the Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Update this to your Kafka server address
}

# Initialize the Producer
producer = Producer(**conf)

# Define the topic
topic = 'quickstart-events'  # Update this to your Kafka topic

def delivery_report(err, msg):
    """ Callback called when a message is delivered or failed. """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

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

# Function to produce and send the message
def produce_message():
    while True:
        # Generate the message
        message = generate_message()
        
        # Convert the message to a JSON string
        message_str = json.dumps(message)
        print(f'Producing message: {message_str}')
        
        # Produce and send the message
        producer.produce(topic, message_str.encode('utf-8'), callback=delivery_report)
        
        # Wait for any outstanding messages to be delivered and report delivery result
        producer.flush()
        time.sleep(0.2)

# Call the produce message function
produce_message()