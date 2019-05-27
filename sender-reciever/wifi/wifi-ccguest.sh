#!/bin/bash
cp /etc/wpa_supplicant/wifi2 /etc/wpa_supplicant/wpa_supplicant.conf
sudo wpa_cli -i wlan0 reconfigure
pid=$(pgrep -f blynk)
sudo kill $pid
