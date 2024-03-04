from confluent_kafka import Consumer, KafkaException
import json

def create_consumer():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }
    return Consumer(conf)

def calculate_price_return(new_price, old_price):
    return (new_price - old_price) / old_price if old_price else None

def consume_messages(consumer, topic_name):
    consumer.subscribe([topic_name])

    # Dictionary to store the last price for each symbol
    last_prices = {}

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

            # Calculate the price return if we have a previous price
            if symbol in last_prices:
                price_return = calculate_price_return(close_price, last_prices[symbol])
                print(f'Symbol: {symbol}, Price Return: {price_return}')
            else:
                print(f'Symbol: {symbol}, Price Return: None (first record)')

            # Update the last price for the symbol
            last_prices[symbol] = close_price

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consumer = create_consumer()
    consume_messages(consumer, 'quickstart-events')
