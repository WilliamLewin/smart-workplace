# 2019-04-16
# Version 1.0.1
# Note: This file should be runned with python run_this.py
# after this file has been runned coordinates will be sent
# no cleaning up is needed program will do that for you.

from serial_rpi import *
import os
os.chdir('/home/pi/sender-reciever/lora/')
os.system('make clean all')
rpi = serial_rpi()
rpi.write_to_file()
os.system('/home/pi/sender-reciever/lora/dragino_lora_app sender')
#os.system('rm /home/pi/sender-reciever/lora/dragino_lora_app')
#os.system('rm /home/pi/sender-reciever/lora/rpi-transceiver-main.o')
#os.system('rm /home/pi/sender-reciever/lora/coordinates')
#os.system('rm /home/pi/sender-reciever/lora/serial_rpi.pyc')
os.system('/home/pi/sender-reciever/lora/clean.sh')
print("Transmitting is done!\n\r")
