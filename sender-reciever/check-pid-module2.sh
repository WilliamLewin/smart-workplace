#!/bin/sh
if ps -ef | grep -v grep | grep blynk-module2.py ; then
  exit 0
else
  python /home/pi/sender-reciever/blynk-module2.py &
  exit 0
fi
