import sys
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='json')

message = '...' + ''.join(sys.argv[1:])
print(' '.join(sys.argv[1:]))
channel.basic_publish(exchange='',
                      routing_key='json',
                      body=message)
print(" [x] Sent %r" % message)

connection.close()