import sys
import os
import time
import re
import math

data = ['5','100','200','300','400','500','600','700','800','900','1000','1100']
for xyz in range(0,len(data)):
    file = open(data[xyz],'r')
    packets = file.read()
    buffer = []

    for i in range(0, len(packets)):
        if packets[i] != '\n':
            buffer.append(packets[i])
    str = ''.join(buffer)
    str = str.replace("5920.1234","")
    str = str.replace(" ","")
    str = str.split("Payload:")
    prssi = []
    rssi = []
    snr = []
    for i in range(0,len(str)-1):
        start = str[i].find("PacketRSSI:")
        end = str[i].find(",RSSI:")
        x = ''.join(str[i][start:end].split("PacketRSSI:"))
        prssi.append(x)

    for i in range(0,len(str)-1):
        start = str[i].find(",RSSI:")
        end = str[i].find(",SNR:")
        y = ''.join(str[i][start:end].split(",RSSI:"))
        rssi.append(y)

    for i in range(0,len(str)-1):
        start = str[i].find("SNR:")
        end = str[i].find(",Length:")
        x = ''.join(str[i][start:end].split("SNR:"))
        snr.append(x)

    prssi = map(int,prssi)
    rssi = map(int,rssi)
    snr = map(int,snr)


    txt = "Range: " + data[xyz] + " meter"
    packet = sum(prssi)/len(prssi)
    recieved = sum(rssi)/len(rssi)
    signal = sum(snr)/len(snr)

    print(txt)
    print("prssi:")
    print(prssi)
    print("\nrssi:")
    print(rssi)
    print(snr)
    print(packet)
    print(recieved)
    print(signal)
