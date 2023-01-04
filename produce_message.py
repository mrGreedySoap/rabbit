import pika, sys, os
import json


def json_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='json')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        message = json.loads(body.decode('utf-8'))
        print(f"message, type: {message}, {type(message)}")

    channel.basic_consume(queue='json', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        json_message()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)