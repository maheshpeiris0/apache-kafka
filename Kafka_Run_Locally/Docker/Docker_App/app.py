from confluent_kafka import Producer
import time

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Producer configuration
conf = {
    'bootstrap.servers': 'kafka:9092',  # Updated to use the hostname 'kafka'
}

producer = Producer(conf)

try:
    for i in range(10):
        producer.produce('quickstart-events', f'message {i}', callback=delivery_report)
        producer.poll(0)
        time.sleep(1)
finally:
    producer.flush(30)
