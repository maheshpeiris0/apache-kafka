from confluent_kafka import Producer
import json
import os

# Kafka configuration
config = {
    'bootstrap.servers': os.environ.get('BOOTSTRAP_SERVERS_CONFLUENT'),  # Replace with your server
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.environ.get('API_KEY_CONFLUENT'),               # Replace with your API key
    'sasl.password': os.environ.get('API_SECRET_CONFLUENT')           # Replace with your API secret
}

# Create Producer instance
producer = Producer(config)

# Produce a message
topic = 'topic_0'
message = {'3': 'message helloE github'}
producer.produce(topic, json.dumps(message))
producer.flush()
