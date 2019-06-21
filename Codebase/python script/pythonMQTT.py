#!/usr/bin/env python2.7
import paho.mqtt.client as mqtt
import mysql.connector
import sys
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("JavaTest");
    
def on_message(client, userdata, msg):
    print(str(msg.payload))
    inString = str(msg.payload)
    if inString[0:12] == "TMP: Room 1 ":
        temp = inString[12:]
        print temp
        stmt = "INSERT INTO airdataRoom1 (airTemp,timestamp,date,time) VALUES ("+temp+", now(), now(), now())"
        mycursor.execute(stmt)
        con.commit();
    elif inString[0:12] == "TMP: Room 2 ":
        temp = inString[12:]
        stmt = "INSERT INTO airdataRoom2 (airTemp,timestamp,date,time) VALUES ("+temp+", now(), now(), now())"
        mycursor.execute(stmt)
        con.commit();
    elif inString[0:12] == "TMP: Room 3 ":
        temp == inString[12:]
        stmt = "INSERT INTO airdataRoom3 (airTemp,timestamp,date,time) VALUES ("+temp+", now(), now(), now())"
        mycursor.execute(stmt)
        con.commit();
con = mysql.connector.connect(user="Homer", password="Baron", host="127.0.0.1", database="smartHouseLongTerm")
mycursor = con.cursor()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.mqttdashboard.com")
client.loop_forever()
