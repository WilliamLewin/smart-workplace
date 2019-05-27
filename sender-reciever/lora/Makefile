 #/*******************************************************************************
 #*
 #* Copyright (c) 2018 Dragino
 #*
 #* http://www.dragino.com
 #*
 #*******************************************************************************/

# dragino lora testing
# Single lora testing app

CC=g++
CFLAGS=-c -Wall
LIBS=-lwiringPi

all: dragino_lora_app

dragino_lora_app: rpi-transceiver-main.o
	$(CC) rpi-transceiver-main.o  $(LIBS) -o dragino_lora_app

rpi-transceiver-main.o: rpi-transceiver-main.c
	$(CC) $(CFLAGS) rpi-transceiver-main.c

clean:
	rm *.o dragino_lora_app
