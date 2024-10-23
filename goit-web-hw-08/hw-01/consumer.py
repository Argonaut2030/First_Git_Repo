import json
import os
import sys
import time

import pika

from models import Contact


def send_email(contact_id): # функція-заглушка для імітації надсилання email
    contact = Contact.objects(id=contact_id).first()
    if contact:
        email_address = contact.email
        print(f" [x] Sending email to {email_address}")
        time.sleep(1)  # delay
    else:
        print(f"Error: Contact with ID {contact_id} not found.")

def main():
    credentials = pika.PlainCredentials("pzgfrxng", "IPbi4tUTASIrVQ1EZGCUYfC20uXPilej")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="hawk-01.rmq.cloudamqp.com",
            port=5672,
            credentials=credentials,
            virtual_host="zpgfrxng",
        )
    )

    channel = connection.channel()
    queue_name = 'web_16_campaign'
    channel.queue_declare(queue=queue_name, durable=True)

    
    def callback(ch, method, properties, body):
        pk = body.decode()
        contact = Contact.objects(id=pk)
        print(f" [x] Received task N {method.delivery_tag} ")
        send_email(pk)    
        if contact:
            contact.update(email_sent=True)
        print(f" [x] Competed task N {method.delivery_tag} ")
        ch.basic_ack(delivery_tag=method.delivery_tag)
   
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
