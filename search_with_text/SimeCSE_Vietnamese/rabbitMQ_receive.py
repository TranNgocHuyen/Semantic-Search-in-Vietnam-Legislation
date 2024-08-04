# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
#!python -m pip install pika --upgrade

import pika
import os
import sys

def main():
    # thiết lập kết nối với máy chủ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Tạo hàng đợi, nơi tin nhắn đc gửi đến
    channel.queue_declare(queue='hello')

    '''
    Kiếm tra danh sách hàng đợi đã tồn tại
    rabbitmqctl.bat list_queues
    '''

    # hàm này sẽ in nội dung của tin nhắn lên màn hình
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        print(" [x] Done")
        #ch.basic_ack(delivery_tag = method.delivery_tag)

    #  cho RabbitMQ biết rằng hàm gọi lại cụ thể này sẽ nhận tin nhắn từ hàng đợi hello
    channel.basic_consume(queue='hello',
                        auto_ack=True, # ?
                        on_message_callback=callback)
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
