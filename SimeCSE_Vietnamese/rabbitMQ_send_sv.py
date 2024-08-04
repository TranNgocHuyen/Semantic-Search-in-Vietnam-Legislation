# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
#!python -m pip install pika --upgrade
import pika
import json

rabbitmq_config = {
    "HostName": "10.0.0.85",
    "UserName": "user",
    "Password": "user",
    "Port": 5672,
    "VirtualHost": "text",
    "QueryQueue": "queue_text_client",
    "ResponseQueue": "queue_text_server"
}
# Kết nối đến RabbitMQ
credentials = pika.PlainCredentials(rabbitmq_config["UserName"], rabbitmq_config["Password"])
parameters = pika.ConnectionParameters(rabbitmq_config["HostName"], rabbitmq_config["Port"], rabbitmq_config["VirtualHost"], credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Tạo hàng đợi nếu chưa tồn tại
channel.queue_declare(queue=rabbitmq_config["QueryQueue"], durable=True)

# -> sẵn sàng gửi tin nhắn
body = 'Day la text anh Khuong gui'
body =  body.encode('utf-8')

channel.basic_publish(exchange='',
                      routing_key=rabbitmq_config["QueryQueue"],  # tên hàng đợi
                      body=body)
print(f" [x] Sent {body}'")

# đóng kết nối:
connection.close()
