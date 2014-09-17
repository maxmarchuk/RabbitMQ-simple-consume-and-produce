#!/usr/bin/env python
import pika
import subprocess 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
    messageToSend = raw_input('Enter message: ')
    if (messageToSend == 'stop') or (messageToSend == 'close') or (messageToSend == 'exit'): 
        print '############################'
        print '##   Closing Provider     ##'
        print '############################'
        break
    else: 
        channel.basic_publish(exchange='', routing_key='hello', body=messageToSend )
        print " [x] Sent '" + messageToSend + "'"

connection.close()
