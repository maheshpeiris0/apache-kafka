from confluent_kafka import Producer
import json

conf = {
    'bootstrap.servers': 'kafka1:9092',  # Adjust to match the EXTERNAL listener
}

producer = Producer(**conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Example: sending a simple message
data = {'number': 123}
producer.produce('newmytopic', json.dumps(data).encode('utf-8'), callback=delivery_report)
producer.flush()
