#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# kafka_producer.py

import json
import requests
from kafka import KafkaProducer

# Set up Kafka producer connection
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Match your Docker Compose service name
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Pull random user data and send to Kafka
for _ in range(10):
    try:
        response = requests.get("https://randomuser.me/api/")
        result = response.json()["results"][0]

        data = {
            "first_name": result["name"]["first"],
            "last_name": result["name"]["last"],
            "email": result["email"]
        }

        print(f"Producing to Kafka: {data}")
        producer.send("user_created", value=data)

    except Exception as e:
        print(f"Error sending data: {e}")

producer.flush()
print("✅ All messages sent to Kafka!")

