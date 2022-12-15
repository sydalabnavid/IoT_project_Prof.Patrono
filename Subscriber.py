##########################################
''' 
Subscriber

MQTT Broker under cloud
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

import json

import sqlite3 as sq3

from flask import Flask, render_template

from tkinter import *

import copy



##########################################

# Subscribing MQTT
brokerAddress = "3f55e02a175d4a0fa14dd4d39c235873.s2.eu.hivemq.cloud"
usernamee = 'client1credential'
passwordd = 'Cred123456'

topic = "Sensor/temperature/tmp5-25-2022"


RealTimeInfo = {}
DataBase = []
Sensordata_touple_time = []
Sensordata_touple_temp = []
realtemp = []
app= Flask(__name__)



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('connected successfully')
    else:
        print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):

    print("Recieved message: " + msg.topic+" -> "+str(msg.payload.decode("utf-8")))
    
    # write to sqlite3 database
    con = sq3.connect('D:\\Training\\IoT_project\\MQTT\\IoT_Project\\Gateway_database\\DataBaseIoTproject.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS EnvironmentalData (Time TEXT PRIMARY KEY, Temperature TEXT )')
    sensordata = json.loads(msg.payload.decode("utf-8"))
    cur.execute('insert into EnvironmentalData values(:Time,:Temperature)', sensordata)

    con.commit()

    cur.execute('select * from EnvironmentalData')
    data = cur.fetchall() 
    # print the database
    # print(data)

    con.close()
    global realtemp 
    global RealTimeInfo
    global DataBase
    RealTimeInfo = copy.copy(sensordata)
    DataBase = copy.copy(data)
    realtemp = sensordata["Temperature"]



@app.route('/')
def start():
    # return '<h1> RealTimeInfo, DataBase  </h1>'
    return render_template(r'index2.html', realtimeT = realtemp)


@app.context_processor
def context_processor():
    Sensordata_touple_time = [row[0] for row in DataBase]
    Sensordata_touple_temp = [row[1] for row in DataBase]
    return dict(key1 = RealTimeInfo, key2 = DataBase, labels = Sensordata_touple_time, values = Sensordata_touple_temp)


# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
# client.username_pw_set(usernamee, passwordd)
# client.connect(brokerAddress, 8883)

# client.subscribe(topic)

# client.loop_forever()

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    client.username_pw_set(usernamee, passwordd)
    client.connect(brokerAddress, 8883)

    client.subscribe(topic)
    client.loop_start()
    app.run(debug=True)
    client.loop_stop()
    

 
if __name__ == '__main__':
    main()


