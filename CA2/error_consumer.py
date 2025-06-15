from kafka import KafkaConsumer

topic_name = 'darooghe.error_logs'
bootstrap_servers = ['localhost:9092']
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='error_consumer_group',
    value_deserializer=lambda x: x.decode('utf-8')
)
for message in consumer:
    print(f"{message.value}")