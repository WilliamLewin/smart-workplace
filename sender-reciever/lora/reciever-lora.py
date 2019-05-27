# 2019-04-16
# Version 1.0.1
# Note: This file should be runned with python reciever-lora.py
# after this file has been runned coordinates will be recieved
# no cleaning up is needed program will do that for you.

from serial_rpi import *
import os
os.chdir('/home/pi/sender-reciever/lora')
os.system('make clean all')
os.system('/home/pi/sender-reciever/lora/dragino_lora_app rec')
rpi = serial_rpi()
rpi.read_from_file()
rpi.distance_check()
#os.system('rm /home/pi/sender-reciever/lora/dragino_lora_app')
#os.system('rm /home/pi/sender-reciever/lora/rpi-transceiver-main.o')
#os.system('rm /home/pi/sender-reciever/lora/serial_rpi.pyc')
#os.system('rm /home/pi/sender-reciever/lora/recCoordinates')
os.system('/home/pi/sender-reciever/lora/clean.sh')
print("Recieving is done!\n\r")
