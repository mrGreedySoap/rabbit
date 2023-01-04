import pika

message = str(0x8544)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='str')
channel.basic_publish(exchange='',
                      routing_key='str',
                      body=message)
print(f" [x] Sent '{message}'")
connection.close()
