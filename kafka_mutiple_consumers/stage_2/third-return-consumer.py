from confluent_kafka import Consumer, KafkaException, Producer
import json
import pandas as pd

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

def calculate_price_return(new_price, old_price):
    return (new_price - old_price) / old_price if old_price else None

def read_old_prices_from_parquet(file_path):
    # Ensure you have gcsfs installed to handle 'gs://' paths
    df = pd.read_parquet(file_path, engine='pyarrow')
    return df.set_index('symbol')['close_price'].to_dict()

def consume_messages(consumer, producer, input_topic_name, output_topic_name, old_prices):
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

            old_price = old_prices.get(symbol, None)
            if old_price is not None:
                price_return = calculate_price_return(close_price, old_price)

                if price_return > 0:  # Check if the return is positive
                    print(f'Symbol: {symbol}, Positive Price Return: {price_return}')
                    message = {
                        'symbol': symbol,
                        'price_return': price_return,
                        'original_data': data
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
    
    # Path to the Parquet file in GCS
    file_path = 'gs://test-data-bucket-mp/stock-data.parquet'
    old_prices = read_old_prices_from_parquet(file_path)
    
    consume_messages(consumer, producer, input_topic_name, output_topic_name, old_prices)
