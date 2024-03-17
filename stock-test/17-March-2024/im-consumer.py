from confluent_kafka import Consumer, KafkaException, OFFSET_BEGINNING
import json
import os
from threading import Thread
import queue

def create_consumer():
    # Consumer configuration with adjustments
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,  # Disable auto commit for manual control
    }
    return Consumer(conf)

def worker(consumer, output_dir, message_queue):
    while True:
        try:
            msg = message_queue.get(timeout=10)  # Adjust timeout as needed
            if msg is None:  # Use None as a signal to stop the thread
                break

            key = msg.key().decode('utf-8') if msg.key() else 'null'
            try:
                value = json.loads(msg.value().decode('utf-8'))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue

            file_path = os.path.join(output_dir, f"{key}.json")
            try:
                with open(file_path, 'a') as file:  # Append mode to reduce opening/closing
                    json.dump(value, file)
                    file.write('\n')  # Newline for separating JSON objects
            except IOError as e:
                print(f"IO error: {e}")

        finally:
            message_queue.task_done()

def consume_messages_to_separate_json(consumer, topic_name, output_dir, num_workers=4):
    consumer.subscribe([topic_name])
    message_queue = queue.Queue()

    # Start worker threads
    workers = [Thread(target=worker, args=(consumer, output_dir, message_queue)) for _ in range(num_workers)]
    for w in workers:
        w.start()

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
            message_queue.put(msg)
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()

        # Signal workers to stop
        for _ in workers:
            message_queue.put(None)
        for w in workers:
            w.join()  # Wait for all workers to finish

        print(f"Messages saved to directory: {output_dir}")

if __name__ == '__main__':
    consumer = create_consumer()
    output_directory = 'stock_by_key'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    consume_messages_to_separate_json(consumer, 'quickstart-events', output_directory)
