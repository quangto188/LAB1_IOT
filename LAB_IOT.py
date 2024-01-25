import sys
from Adafruit_IO import MQTTClient
import time
import random
AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "todiuquang123"
AIO_KEY = "aio_oyvC28eVXIPS918x0mkj0KH1FZhy"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + "feed id:"  + feed_id) 

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter=10
while True:
    counter = counter -1
    if counter <=0:
        counter =10
        print("Random data is publishing...")
        temp = random.randint(10,20)
        client.publish("cambien1", temp)
        humi = random.randint(40,60)
        client.publish("cambien2", humi)
        light = random.randint(100,500)
        client.publish("cambien3", light)

    time.sleep(1)
    pass
