from kafka import KafkaProducer
import json
from data_generator import generate_data
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'], value_serializer=json_serializer)

if __name__ == "__main__":
    while 1:
        registered_user = generate_data()
        print(registered_user)
        producer.send("myFirstTopic", registered_user)
        time.sleep(5)
