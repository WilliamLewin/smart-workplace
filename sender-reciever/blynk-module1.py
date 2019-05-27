# 2019-04-16
# Version 1.0.0

import blynklib
import sys
import math
import os
import numbers
from lora.serial_rpi import serial_rpi

file = open('/home/pi/sender-reciever/key','r')
buffer = file.read()
key =[]
for i in range(0,len(buffer)):
    if '\n' not in buffer[i]:
        key.append(buffer[i])
key = ''.join(key)
BLYNK_AUTH = key
blynk = blynklib.Blynk(BLYNK_AUTH)

def getCoordinates():
    rpi = serial_rpi()
    coordinates = rpi.filter_coordinates()
    print(coordinates)
    if (coordinates[0]=='' or coordinates[1]==''):
        lat = 0
        long = 0
        #blynk.virtual_write(16,1,lat,long,"M1")
        #blynk.virtual_write(20, lat)
        #blynk.virtual_write(21, long)
    else:
        lat = coordinates[0]
        long = coordinates[1]
        x1 = lat[0:2]
        x2 = lat[2:9]
        lat = float(x1) + float(x2)/60
        y1 = long[0:3]
        y2 = long[3:10]
        long = float(y1) + float(y2)/60
        #blynk.virtual_write(16,1,lat,long,"M1")
        #blynk.virtual_write(20, lat)
        #blynk.virtual_write(21, long)
    return lat, long

def getPeformanceMetrics():
    #file = open('peformance_metrics','r')
    #buffer1 = file.read()
    #buffer2 = []
    #for i in range(0,len(buffer1)):
    #    if '\n' not in buffer1[i]:
    #        buffer2.append(buffer1[i])
    #buffer2 = ''.join(buffer2)
    #buffer2 = buffer2.replace(" ","")
    #buffer2 = buffer2.split("min")
    #snr = ''.join(filter(str.isdigit, buffer2[0]))
    #rssi1 = ''.join(filter(str.isdigit, buffer2[1]))
    #rssi2 = ''.join(filter(str.isdigit, buffer2[2]))
    file = open('peformance_metrics','r')
    buffer1 = file.read()
    buffer2 = []
    for i in range(0,len(buffer1)):
        if '\n' not in buffer1[i]:
            buffer2.append(buffer1[i])
    buffer2 = ''.join(buffer2)
    buffer2 = buffer2.replace(" ","")
    buffer2 = buffer2.replace("SNR:", "")
    buffer2 = buffer2.replace("PacketRSSI:", "")
    buffer2 = buffer2.replace("RSSI:", "")
    buffer2 = buffer2.split("min")
    snr = buffer2[0]
    rssi1 = buffer2[1]
    rssi2 = buffer2[2]
    return snr, rssi1, rssi2

def writeToBlynkApp():
    latLong = getCoordinates()
    peformanceMetrics = getPeformanceMetrics()
    blynk.virtual_write(16,1,latLong[0],latLong[1],"M1")
    blynk.virtual_write(19, peformanceMetrics[0])
    blynk.virtual_write(20, peformanceMetrics[1])
    blynk.virtual_write(21, peformanceMetrics[2])


while True:
    blynk.run()
    writeToBlynkApp()
