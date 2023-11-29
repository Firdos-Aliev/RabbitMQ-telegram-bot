import pika
import os


class MessageQueue():

    def __init__(self, host, port, virtual_host, user, password):

        credentials = pika.PlainCredentials(user, password)
        self.connection_parameters = pika.ConnectionParameters(
            host=host,
            port=port,
            virtual_host=virtual_host,
            credentials=credentials,
            heartbeat=0
            )
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()

        # channels
        self.channel.queue_declare(queue='0')


    async def publish_message(self, message):
        self.channel.basic_publish(exchange="", routing_key="0", body=message)

    
    def __del__(self):
        self.connection.close()

