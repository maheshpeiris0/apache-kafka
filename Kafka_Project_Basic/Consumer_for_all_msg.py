from confluent_kafka import Consumer, KafkaError
import os

# Kafka configuration
config = {
    'bootstrap.servers': os.environ.get('BOOTSTRAP_SERVERS'),  # Replace with your server
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.environ.get('SASL_USERNAME'),  # Replace with your API key
    'sasl.password': os.environ.get('SASL_PASSWORD'),  # Replace with your API secret
    'group.id': 'my_group',  # Consumer group ID
    'auto.offset.reset': 'latest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer = Consumer(config)
consumer.subscribe(['topic_0'])

# Poll messages
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of partition")
            else:
                print(f"Consumer error: {msg.error()}")
        else:
            print(f"Received message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Consumer stopped by user")
finally:
    consumer.close()
