# Smart Workplace

## This file contains instructions for both the modules.

Setup is needed following [LoRa/GPS hat wiki.](http://wiki.dragino.com/index.php?title=Lora/GPS_HAT) for GPS.

### For GPS and LoRa connection between two modules (http://wiki.dragino.com/index.php?title=Lora/GPS_HAT):
1. Get the latest update from Smart Workplace on GitHub.
2. Unzip folder "sender-reciever" in /home/pi.
3. Do the following commands:
```sh 
cd /home/pi/sender-reciever/ && chmod +x cleaner.sh check-pid-module1.sh check-pid-module2.sh
cd /home/pi/sender-reciever/lora/ && chmod +x clean.sh
cd /home/pi/sender-reciever/wifi/ && chmod +x wifi-ccguest.sh wifi-ccguest.sh cleanup.sh  
```
4. Make two files called wifi1 and wifi2 in /etc/wpa_supplicant/
Wifi1 should contain the hotspot connection, for example look below.
```sh
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=INSERTCOUNTRYCODE

network={
	ssid="HOTSPOTNAME"
	psk="HOTSPOTSECRET"
	key_mgmt=WPA-PSK
}
```
Do the same with wifi2, this should have the original WiFi connection when first installed the Raspberry.

#### Blynk Configuration https://github.com/blynkkk for Python
5. Run the commands below: 
```sh
sudo pip install blynklib 
sudo pip install geopy
```
6. Make an local server https://github.com/blynkkk/blynk-server and follow instructions for Raspberry-Pi. When sucessfully installed or runned the local server, exit the running program.
7. Use ``` cd /home/pi/sender-reciever/ ``` then make a file called key ``` nano key ``` and add the auth-key that was provided upon registration.
8. In the app set out the widget that is needed with the correct virtual pins.
#### GPS Configuration
9. Now you need to change some code lines in some files, follow the commands from below and add what needs to be added:
```sh
sudo nano /boot/config.txt
```
Add ``` enable_uart=1 ``` line, preferly to be the last line.
```sh
sudo nano /boot/cmdline.txt
```
Modify the file to look like: ``` dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait ```
```sh
sudo systemctl disable hciuart
```
One more file needs to be modified.
```sh
sudo nano /lib/systemd/system/hciuart.service
```
Replace ``` After=dev-serial1.device ``` with ``` After=dev-ttyS0.device ```
10. Now there is need of an update
```sh
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```
11. After it has rebooted, we need to disable the service so run the following commands:
```sh
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
```
#### Crontab Configuration
12. Add the lines from under in "crontab -e":
```sh
@reboot python /home/pi/sender-reciever/cleaner.sh >> /home/pi/clean.log 2>&1
@reboot java -jar /home/pi/server-0.41.5-java8.jar -dataFolder /home/pi/Blynk &
*/1 * * * * python /home/pi/sender-reciever/lora/XXXX.py >> /home/pi/myjob.log 2>&1
*/1 * * * * sudo python /home/pi/sender-reciever/wifi/wifi.py >> /home/pi/wifilog.log 2>&1
*/1 * * * * /home/pi/sender-reciever/check-pid-XXXX.sh >> /home/pi/blynk.log 2>&1
```
Where XXXX.py is either module1.py or module2.py.
Where check-pid-XXXX.sh is either check-pid-module1.sh or check-pid-module2.sh.
The first line can be included but in current version it has been a problem with it creating a Read-Only file. So in this version this line is not included in cron jobs.

#### Raspberry Pi Configuration
13. Raspberry pi SPI needs to be activated. This can be done in settings or using Raspi-config.
14. Do the following from below for SSH set hostname:
``` sudo raspi-config ``` and then navigate to "Network" tab, choose "hostname" change the hostname to: SmartWorkplace-moduleX, where X is the number on the module.
