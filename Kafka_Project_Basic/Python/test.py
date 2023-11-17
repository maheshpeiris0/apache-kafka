from confluent_kafka import Producer
import json
import os
import random
import uuid

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

j_value=random_data()

print(j_value)
