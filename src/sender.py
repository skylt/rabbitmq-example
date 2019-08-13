#! /usr/bin/env python

import os
import pika
import time

def rabbitmq_login(user, password):
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters('example-rabbitmq',
                                           5672,
                                           '/',
                                           credentials)
    return pika.BlockingConnection(parameters)

if __name__ == "__main__":
    print(os.environ)
    connection = rabbitmq_login(os.environ["RABBITMQ_DEFAULT_USER"],os.environ["RABBITMQ_DEFAULT_PASS"])
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    body = 'Hello !'
    while True:
        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body)
        print(f"[x] Sent {body}")
        time.sleep(3)

