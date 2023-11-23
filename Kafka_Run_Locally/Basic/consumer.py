from confluent_kafka import Consumer, KafkaException

def create_consumer():
    # Consumer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',  # Use a unique group ID for your consumer
        'auto.offset.reset': 'earliest'  # To read messages from the beginning if the group is new
    }

    return Consumer(conf)

def consume_messages(consumer, topic_name):
    # Subscribe to topic
    consumer.subscribe([topic_name])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:  # No message available within timeout
                continue
            if msg.error():  # Error or event
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    # End of partition event
                    continue
                else:
                    print(msg.error())
                    break
            print(f'Received message: {msg.value().decode("utf-8")}')

    except KeyboardInterrupt:
        pass
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

if __name__ == '__main__':
    consumer = create_consumer()
    consume_messages(consumer, 'quickstart-events')
