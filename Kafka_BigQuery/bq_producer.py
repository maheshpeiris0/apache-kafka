from confluent_kafka import Producer
import os
import json
import time
import random


def random_data():
    emp_id = random.randint(1,1000000)
    first_name = random.choice(['John','Smith','Linda','Sarah','David','James','Robert','Michael','Maria','Mary','Mari','Anna','Emma','Julia','Julie','Samantha','Sara','Sandra','Sofia','Sophia','Sofie','Sofy','Sofe','Sof','Sara','Sar','Sa','S'])
    last_name = random.choice(['Brown','White','Black','Green','Yellow'])
    age = random.randint(20,60)
    department = random.choice(['IT','HR','Finance','Marketing','Sales','Operations','Procurement'])
    salary = random.randint(55000,500000)
    data = {'emp_id':emp_id,'first_name':first_name,'last_name':last_name,'age':age,'department':department,'salary':salary
    }

    return json.dumps(data)

# Kafka configuration
config = {
    'bootstrap.servers': os.environ.get('BOOTSTRAP_SERVERS_CONFLUENT'),  # Replace with your server
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.environ.get('API_KEY_CONFLUENT'),               # Replace with your API key
    'sasl.password': os.environ.get('API_SECRET_CONFLUENT')           # Replace with your API secret
}   

# Create Producer instance
producer = Producer(config)


# Produce a message
# Produce a message
topic = 'topic_0'
while True:
    time.sleep(5)
    kafka_msg = random_data()
    print(kafka_msg)
    producer.produce(topic, kafka_msg)
    producer.flush()