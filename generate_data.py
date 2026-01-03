import csv
import random
import time
from faker import Faker
import datetime

fake = Faker()

TOTAL_RECORDS = 5000000 
FILENAME = 'ecommerce_orders_5million.csv'

def generate_data():
    print(f"Starting Generate {TOTAL_RECORDS} Records ")
    start_time = time.time()

    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        
        writer.writerow(['id', 'order_sn', 'user_id', 'category_id', 'amount', 'status', 'created_at'])

        
        for i in range(1, TOTAL_RECORDS + 1):
            # id 
            order_id = i
            
            # order_sn
            order_sn = f"ORD-{fake.date_between(start_date='-2y', end_date='today').strftime('%Y%m%d')}-{fake.pystr(min_chars=6, max_chars=6).upper()}"
            
            # user_id
            user_id = random.randint(1, 50000)
            
            # category_id
            category_id = random.randint(1, 100)
            
            # amount
            amount = round(random.uniform(10, 5000), 2)
            
            # status: 0-5
            status = random.randint(0, 5)
            
            # created_at
            created_at = fake.date_time_between(start_date='-2y', end_date='now')

            writer.writerow([order_id, order_sn, user_id, category_id, amount, status, created_at])

            if i % 100000 == 0:
                print(f"Generated {i} Records")

    end_time = time.time()
    print(f"Complete! Generated {TOTAL_RECORDS} Records,Execution Time:{end_time - start_time:.2f} 秒")
    print(f"Data Save As: {FILENAME}")

if __name__ == "__main__":
    generate_data()