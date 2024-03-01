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
topic = 'your_topic_name'  # Update this to your Kafka topic

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
        "symbol": "PLUG",
        "volume": random.randint(50, 150),  # Example: Random volume between 50 and 150
        "accumulated_volume": random.randint(20000000, 30000000),  # Example: Random accumulated volume
        "official_open_price": round(random.uniform(2.0, 3.5), 2),  # Example: Random open price between 2.0 and 3.5
        "vwap": round(random.uniform(2.5, 3.5), 3),  # Example: Random VWAP between 2.5 and 3.5
        "open": round(random.uniform(2.5, 3.5), 3),
        "close": round(random.uniform(2.5, 3.5), 3),
        "high": round(random.uniform(2.5, 3.5), 3),
        "low": round(random.uniform(2.5, 3.5), 3),
        "aggregate_vwap": round(random.uniform(2.0, 3.0), 4),
        "average_size": random.randint(50, 150),
        "start_timestamp": round(time.time() * 1000),  # Current time in milliseconds
        "end_timestamp": round(time.time() * 1000 + 1000),  # Current time + 1 second in milliseconds
        "otc": None
    }

# Function to produce and send the message
def produce_message():
    # Generate the message
    message = generate_message()
    
    # Convert the message to a JSON string
    message_str = json.dumps(message)
    print(f'Producing message: {message_str}')
    
    # Produce and send the message
    producer.produce(topic, message_str.encode('utf-8'), callback=delivery_report)
    
    # Wait for any outstanding messages to be delivered and report delivery result
    producer.flush()

# Call the produce message function
produce_message()
