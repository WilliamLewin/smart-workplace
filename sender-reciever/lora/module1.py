# 2019-04-16
# Version 1.0.1

import os
import time

start = time.time()
run = 1
while (time.time() - start) < 57:
    if ((time.time() - start) < 25) and run == 1:
        os.system('python /home/pi/sender-reciever/lora/reciever-lora.py')
        run = 0
    if((time.time() - start) > 27) and run == 0:
        os.system('python /home/pi/sender-reciever/lora/transmit-lora.py')
        run = 1
    time.sleep(1)

print("Run completed!")
print("Time for running:")
print(time.time() - start)
print("\n\r")
