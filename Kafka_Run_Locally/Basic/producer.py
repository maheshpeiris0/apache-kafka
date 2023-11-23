from confluent_kafka import Producer
import time

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Producer configuration
# See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
conf = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(conf)

try:
    for i in range(10):
        producer.produce('quickstart-events', f'message {i}', callback=delivery_report)
        # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered.
        producer.poll(0)
        time.sleep(1)
finally:
    # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered.
    producer.flush(30)
