from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "myFirstTopic",
        bootstrap_servers="127.0.0.1:9092",
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting consumer")
    for msg in consumer:
        print(f"Record = {json.loads(msg.value)}")
