#! /usr/bin/env python

import os
import pika

def rabbitmq_login(user, password):
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters('example-rabbitmq',
                                           5672,
                                           '/',
                                           credentials)
    return pika.BlockingConnection(parameters)


def callback(ch, method, properties, body):
    print(f"[x] Received {body}")


if __name__ == "__main__":
    connection = rabbitmq_login(os.environ["RABBITMQ_DEFAULT_USER"],os.environ["RABBITMQ_DEFAULT_PASS"])
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)
    channel.start_consuming()

