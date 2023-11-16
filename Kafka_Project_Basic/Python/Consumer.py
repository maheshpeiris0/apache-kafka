from confluent_kafka import Consumer
import os
# Kafka configuration
config = {
    'bootstrap.servers': os.environ.get('BOOTSTRAP_SERVERS_CONFLUENT'), # Replace with your server
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username':  os.environ.get('API_KEY_CONFLUENT'),              # Replace with your API key
    'sasl.password': os.environ.get('API_SECRET_CONFLUENT')  ,         # Replace with your API secret
    'group.id': 'my_group',                                  # Consumer group ID
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(config)
consumer.subscribe(['topic_0'])

# Poll messages
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    print(f"Received message: {msg.value().decode('utf-8')}")

consumer.close()
