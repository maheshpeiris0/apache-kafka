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

j_value=random_data()

print(j_value)
