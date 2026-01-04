from kafka import KafkaConsumer
from fraud_rules import is_fraud
import json, os
import sqlite3 as sql_con

DB_PATH = os.path.join(os.path.dirname(__file__), 'fraud_db.db')

consumer = KafkaConsumer('transaction', bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                         )


def db_connect(DB_PATH):
    try:
        sql_conn = sql_con.connect(DB_PATH)
        cursor = sql_conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS transactions ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_id TEXT,
                user_id TEXT,
                amount INTEGER,
                location TEXT,
                timestamp TEXT);""")

        sql_conn.commit()
        print("Database connected successfully")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

# initialize database connection and create table transaction
db_connect(DB_PATH)

try:
    sql_conn = sql_con.connect(DB_PATH)
    cursor = sql_conn.cursor()


    for message in consumer:
        tx = message.value
        fraud, reason = is_fraud(tx)
        print(fraud, reason)


        cursor.execute(
            "INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?, ?)",
            (tx['transaction_id'], tx['user_id'], tx['amount'], tx['location'], tx['timestamp']))
        sql_conn.commit()
        print("Processed:", tx["transaction_id"], "Fraud:", fraud)

finally:
    sql_conn.close()





