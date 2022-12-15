##########################################
''' 
Publisher

HiveMQ Cloud 
https://www.hivemq.com/mqtt-cloud-broker/

Client 
mqttx.app

Cluster connection settings
Name = Client1
Clent ID = Random Name Created by MQTTX app
Host => mqtts://  +  Cluster URL
Port = 8883
Username = HiveMQ Cloud/Cluster Detail/Active MQTT Credentials/Access Management/username
Password = Cred123456

SSL/TLS on
check => CA signed server

'''
##########################################
import paho.mqtt.client as mqtt
import random
import time
import json


brokerAddress = "3f55e02a175d4a0fa14dd4d39c235873.s2.eu.hivemq.cloud"
usernamee = 'client1credential'
passwordd = 'Cred123456'

topic = "Sensor/temperature/tmp5-25-2022"

min = 22
max = 44


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('connected successfully')
    else:
        print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print("Recieved message: " + msg.topic+" -> "+str(msg.payload.decode("utf-8")))  

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(usernamee, passwordd)
client.connect(brokerAddress, 8883)

wait = 5
# Creating a series of data of in range of 22-44 (Lecce in August).


while True:
    QTT_MSG=json.dumps({"Time": time.time(),"Temperature":  round(random.triangular(min, max),2)});
    # dataDigit = [time.time(), random.randint(min,max)]
    # data = str(dataDigit)
    print(QTT_MSG)
    client.publish(topic, QTT_MSG) # change QTT_MSG => data
    time.sleep(wait)
