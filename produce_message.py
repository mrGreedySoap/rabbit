import pika, sys, os



def string_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='str')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        print(f"body to str -> {body.decode('utf-8')},{type(str(body))}")

    channel.basic_consume(queue='str', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def json_message():


if __name__ == '__main__':
    try:
        string_message()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)