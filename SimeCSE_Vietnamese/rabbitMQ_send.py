# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
#!python -m pip install pika --upgrade
import pika
import json

# thiết lập kết nối với máy chủ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Tạo hàng đợi, nơi tin nhắn đc gửi đến
channel.queue_declare(queue='hello')

# -> sẵn sàng gửi tin nhắn
body = [{"text":'Day la text anh Khuong gui'}]

body = json.dumps(body) 
channel.basic_publish(exchange='',
                      routing_key='hello',  # tên hàng đợi
                      body=body)
print(f" [x] Sent {body}'")

# đóng kết nối:
connection.close()
