# check this file in raw format for better visual effect (tree map)

# IoT_project_Prof.Patrono
The project of employing MQTT to recieve the data from sensor in the edge + subscribing the data and save in SQlite + dashboard (HTML) and a pop up warning for high temprature


# Subscribing MQTT
brokerAddress = "3f55e02a175d4a0fa14dd4d39c235873.s2.eu.hivemq.cloud"
usernamee = 'client1credential'
passwordd = 'Cred123456'
topic = "Sensor/temperature/tmp5-25-2022"

=================================================

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
Password = "Written in email"

SSL/TLS on
check => CA signed server

==================================================

graphical illustration of the folder structure

Drive:.
│   Publisher.py
│   Subscriber.py
│
├───Gateway_database
│       DataBaseIoTproject.db
│
└───templates
    │   index2.html
    │
    └───fig
            clouds.jpg

==================================================

line 69 should be modified"
con = sq3.connect('[the path]\\Gateway_database\\DataBaseIoTproject.db')



=================================================
Run the script:
0 clone the reposuitory
1st run the publisher
2nd run the subscriber
3rd open the browser and check out the local host at gate 5000 : 127.0.0.1:5000
4h wait to see the high temprature pop up notification 

Note
- the temprature value is created in random way
- the range of temprature is set between 22 and 44
- The temprature threshold for warning is 40 
