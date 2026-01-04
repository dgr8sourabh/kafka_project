from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8')
                         )

locations = ["India", "USA", "UK"]

while True:
    transaction = {
        "transaction_id": f"tx{random.randint(1000,9999)}",
        "user_id": f"user{random.randint(1,5)}",
        "amount": random.randint(100, 20000),
        "location": random.choice(locations),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.send('transaction', transaction)
    print("Sent:", transaction)
    time.sleep(2)