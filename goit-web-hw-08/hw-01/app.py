import json
from datetime import datetime
from faker import Faker

import pika

from models import Contact

fake = Faker('en_US')


credentials = pika.PlainCredentials("zpgfrxng", "IPbi4tUTASIrVQ1EZGCUYfC20uXPilej")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="hawk-01.rmq.cloudamqp.com",
        port=5672,
        credentials=credentials,
        virtual_host="zpgfrxng",
    )
)


channel = connection.channel()

exchange = "Web16 Service"
queue_name = "web_16_campaign"

channel.exchange_declare(exchange=exchange, exchange_type="direct")
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange, queue=queue_name)


def create_contacts(nums: int):
    for i in range(nums):
        contact = Contact(full_name = fake.name(),
                          email = fake.email(), 
                          email_sent = False, 
                          country = fake.country()
                          ).save()
        channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()


if __name__ == "__main__":
    create_contacts(2)
