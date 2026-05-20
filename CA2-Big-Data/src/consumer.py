from kafka import KafkaConsumer,KafkaProducer
import json
from datetime import datetime, timezone,timedelta




def amount_consistency_is_valid(transaction):
    amount = transaction["amount"]
    commission_amount = transaction["commission_amount"]
    vat_amount = transaction["vat_amount"]
    total_amount = transaction["total_amount"]
    if amount + commission_amount + vat_amount == total_amount:
        return True
    else:
        print(1)
        return False

def time_warping_is_valid(message):
    transaction = message.value
    kafka_ingestion_time = message.timestamp
    transaction_timestamp = transaction["timestamp"]

    transaction_time = datetime.fromisoformat(
        transaction_timestamp.replace("Z", "+00:00"))
    ingestion_time = datetime.fromtimestamp(
        kafka_ingestion_time / 1000, timezone.utc)
    max_age = timedelta(days=1)
    if transaction_time > datetime.now(timezone.utc):
        return False,"Transaction in Future"
    if (ingestion_time - transaction_time) > max_age:
        return False,"Transaction Time is old"
    return True,None

def device_info_is_valid(transaction):
    if transaction["payment_method"] == "mobile" and (transaction["device_info"]["os"] not in ["Android", "iOS"]):
        return False
    return True
        
def verify_transaction(message,producer):
    is_valid_transaction=True
    is_valid_time,error_message = time_warping_is_valid(message)
    if not amount_consistency_is_valid(message.value):
        error_message = {
            "Error_Code": "ERR_AMOUNT",
            "transaction_id": message.value["transaction_id"],
            "Error_Message": "Amount Consistency Error",
        }
        producer.send('darooghe.error_logs', error_message)
        is_valid_transaction=False
    if not device_info_is_valid(message.value):
        error_message = {
            "Error_Code": "ERR_DEVICE",
            "transaction_id": message.value["transaction_id"],
            "Error_Message": "Device Info Error",
        }
        producer.send('darooghe.error_logs', error_message)
        print("sending error message3")
        is_valid_transaction=False
    if not is_valid_time:
        error_message = {
            "Error_Code": "ERR_TIME",
            "transaction_id": message.value["transaction_id"],
            "Error_Message": error_message,
        }
        producer.send('darooghe.error_logs', error_message)
        is_valid_transaction=False
    
    return is_valid_transaction

consumer = KafkaConsumer(
    'darooghe.transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True
)
producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
for message in consumer:
    if (verify_transaction(message,producer)):
     print(json.dumps(message.value))
        
