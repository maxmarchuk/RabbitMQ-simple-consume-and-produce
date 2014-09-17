#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    if body.lower() == 'close receiver':
        print '############################'
        print '## Recieved close command ##'
        print '############################'
        channel.stop_consuming() 
        return 
    print " [x] Received %r" % (body,)

channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
