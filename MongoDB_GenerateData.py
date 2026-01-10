import json
import random
from faker import Faker
from datetime import datetime

fake = Faker()


TOTAL_RECORDS = 10000000  
FILE_NAME = "orders_data_10Million.json"
BATCH_SIZE = 100000      


STATUS_OPTIONS = ["shipped", "pending", "cancelled", "delivered"]

STATUS_WEIGHTS = [0.15, 0.1, 0.05, 0.7] 

print(f"start generating {TOTAL_RECORDS} records...")

start_time = datetime.now()

with open(FILE_NAME, 'w', encoding='utf-8') as f:
    for i in range(TOTAL_RECORDS):
        
        record = {
            "order_id": f"ORD-{fake.uuid4()[:13].upper()}",
            "user_id": random.randint(10000, 99999),
            "status": random.choices(STATUS_OPTIONS, weights=STATUS_WEIGHTS)[0],
            "amount": round(random.uniform(10.0, 2000.0), 2),
            "created_at": fake.date_time_between(start_date='-2y', end_date='now').isoformat(),
            "priority": random.randint(1, 5)
        }
        
       
        f.write(json.dumps(record) + '\n')
        
        if (i + 1) % BATCH_SIZE == 0:
            print(f"Generated {i + 1} ")

end_time = datetime.now()
print(f"Done! Execution Time: {end_time - start_time}")
print(f"Save As: {FILE_NAME}")