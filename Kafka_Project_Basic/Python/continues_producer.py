from confluent_kafka import Producer
import json
import os
import random
import uuid

def random_data():
    key =  random.randint(1,6)
    value = uuid.uuid4().hex
    data = {'key':key,'value':value
    }

    return json.dumps(data)

# Kafka configuration
config = {
    'bootstrap.servers': os.environ.get('BOOTSTRAP_SERVERS'),  # Replace with your server
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.environ.get('SASL_USERNAME'),               # Replace with your API key
    'sasl.password': os.environ.get('SASL_PASSWORD')           # Replace with your API secret
}

# Create Producer instance
producer = Producer(config)

# Produce a message
topic = 'topic_0'
message = {'5': 'message hello test'}
producer.produce(topic, random_data())
producer.flush()