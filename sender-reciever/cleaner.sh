#!/bin/bash
cd /home/pi/
sudo rm wifilog.log && sudo rm myjob.log && sudo rm blynk.log
sudo rm /home/pi/sender-reciever/lora/coordinates
sudo rm /home/pi/sender-reciever/lora/serial_rpi.pyc
sudo rm /home/pi/sender-reciever/lora/recCoordinates
sudo rm /home/pi/sender-reciever/lora/__init__.pyc
sudo rm /home/pi/sender-reciever/lora/dragino_lora_app
sudo rm /home/pi/sender-reciever/lora/rpi-transceiver-main.o
sudo rm /home/pi/testingDayTwo/counterValue
sudo rm /home/pi/testingDayTwo/recCounterValues
cd /home/pi/sender-reciever/lora/
make
