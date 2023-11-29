import pika
import json
import requests
import os

from dotenv import load_dotenv

load_dotenv()


def on_message_callback(ch, method, properties, body):
    body = json.loads(body)
    if body["command"] == "print":
        print(f"Last message was: {body}")
    elif body["command"] == "send":
        print(f"Last message was: {body}")
        request = requests.post(
            body["url"], 
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'},
            data=json.dumps({"last_message": body["last_message"]}))
        print(f"Response code: {request.status_code}")


host=os.environ.get("AMQP_ADDRESS", "localhost")
port=os.environ.get("AMQP_PORT", 5672)
virtual_host=os.environ.get("AMQP_VHOST", "/")
user=os.environ.get("AMQP_USER", "guest")
password=os.environ.get("AMQP_PASSWORD", "guest")

credentials = pika.PlainCredentials(user, password)
connection_parameters = pika.ConnectionParameters(
    host=host,
    port=port,
    virtual_host=virtual_host,
    credentials=credentials,
    heartbeat=0
)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='0')

channel.basic_consume(queue='0', on_message_callback=on_message_callback, auto_ack=True)

channel.start_consuming()