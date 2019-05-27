#!/bin/sh
if ps -ef | grep -v grep | grep blynk-module1.py ; then
  exit 0
else
  python /home/pi/sender-reciever/blynk-module1.py &
  exit 0
fi
