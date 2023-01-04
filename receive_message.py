import pika
import json

json_dict = {"Date": "2016-05-21T21:35:40Z",
             "CreationDate": "2012-05-05",
             "LogoType": "png",
             "Ref": 164611595,
             "Classe": ["Email addresses", "Passwords"],
             "Link": "http://some_link.com"}

message = json.dumps(json_dict)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='json')
channel.basic_publish(exchange='',
                      routing_key='json',
                      body=message)
print(f" [x] Sent '{message}'")
connection.close()

