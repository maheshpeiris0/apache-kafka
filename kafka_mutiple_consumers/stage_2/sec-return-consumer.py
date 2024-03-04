from confluent_kafka import Consumer, KafkaException, Producer
import json

def create_consumer():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }
    return Consumer(conf)

def create_producer():
    conf = {
        'bootstrap.servers': 'localhost:9092'
    }
    return Producer(conf)

def produce_message(producer, topic_name, message):
    producer.produce(topic_name, value=json.dumps(message))
    producer.flush()

def calculate_price_return(new_price, old_price=2):
    # Assuming all old prices as 1 as per the new requirement
    return (new_price - old_price) / old_price if old_price else None

def consume_messages(consumer, producer, input_topic_name, output_topic_name):
    consumer.subscribe([input_topic_name])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            data = json.loads(msg.value().decode('utf-8'))
            symbol = data['symbol']
            close_price = data['close']

            # Calculate the price return with an old price assumed as 1
            price_return = calculate_price_return(close_price)

            if price_return > 0:  # Check if the return is positive
                print(f'Symbol: {symbol}, Positive Price Return: {price_return}')
                # Construct a message to be sent to the next stage including original data
                message = {
                    'symbol': symbol,
                    'price_return': price_return,
                    'original_data': data  # Including the original data in the message
                }
                print(message)
                produce_message(producer, output_topic_name, message)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consumer = create_consumer()
    producer = create_producer()
    input_topic_name = 'quickstart-events'
    output_topic_name = 'positive-returns'
    consume_messages(consumer, producer, input_topic_name, output_topic_name)
