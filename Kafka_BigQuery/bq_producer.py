from confluent_kafka import Producer
import os
import json
import time
import random

def random_data():
    key =  random.randint(0,5)
    value = random.randint(0,100)
    data = {'key':key,'value':value
    }

    return json.dumps(data)