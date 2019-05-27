# 2019-04-16
# Version: 1.0.1

import time
import serial
import geopy.distance
import math

class serial_rpi:

    ###################################
    # This function captures GPS data
    # using serial port /dev/ttyS0
    # which the LoRa/GPS hat has gps
    # module connected on.
    #
    # Return: GPS data
    ###################################

    def capture_gps_data(self):
        gpsBuffer = []
        serial_gps = serial.Serial('/dev/ttyS0')
        serial_gps.baudrate = 9600
        end_time = 8                               #run for 10 seconds
        stop_time = None                            #stop time variable
        start = time.time()
        while stop_time < end_time:
            stop = time.time()
            stop_time = stop - start
        serial_read = serial_gps.inWaiting()
        gpsBuffer = serial_gps.read(serial_read)
        return gpsBuffer

    ###################################
    # This function filters out
    # gps data that is being transmit-
    # ted.
    #
    # Return: Filtered GPS data
    ###################################

    def filter_gps_data(self):
        dataBuffer = []
        i = 0
        gpsBuffer = self.capture_gps_data()
        datastr = []
        while i < len(gpsBuffer):
            if '\r' not in gpsBuffer[i]:
                datastr.append(gpsBuffer[i])
            else:
                if '$GPRMC' in ''.join(datastr):
                    dataBuffer.append(''.join(datastr))
                    datastr = []
                else:
                    datastr = []
            i = i + 1
        return dataBuffer

    ###################################
    # This function gives latitude
    # and longtitude
    #
    # Return: Latitude and longtitude
    ###################################
    def filter_coordinates(self):
        longtitude = 0
        latitude = 0
        dataBuffer = self.filter_gps_data()
        cleanedBuffer = []
        for i in range(0,len(dataBuffer)):
            cleanedBuffer = dataBuffer[i].split(",")
            latitude = cleanedBuffer[3]
            longtitude = cleanedBuffer[5]
        coordinates = [latitude,longtitude]
        return coordinates

    ###################################
    # This function writes latitude
    # and longtitude to a file called
    # coordinates
    # Return: None
    ###################################

    def write_to_file(self):
        coordinates = self.filter_coordinates()
        file = open("/home/pi/sender-reciever/lora/coordinates","w")
        file.write(str(coordinates[0]))
        file.write('\n\r')
        file.write(str(coordinates[1]))
        file.close()


    def read_from_file(self):
        file = open('/home/pi/sender-reciever/lora/recCoordinates','r')
        coordinates = file.read()
        buffer = []
        for i in range(0,len(coordinates)):
            if coordinates[i] != '\n':
                buffer.append(coordinates[i])
        cleanedBuffer = ''.join(buffer)
        latitude = cleanedBuffer[0:9]
        longtitude = cleanedBuffer[9:20]
        latLong = [latitude,longtitude]
        return latLong

    def calculate_dist_gps(self):
        latLong = self.filter_coordinates()
        #Changed Code
        lat = latLong[0]
        long = latLong[1]
        x1 = lat[0:2]
        x2 = lat[2:9]
        lat = float(x1) + float(x2)/60
        y1 = long[0:3]
        y2 = long[3:10]
        long = float(y1) + float(y2)/60
        #latitude1 = float(latLong[0])/100
        #longtitude1 = float(latLong[1])/100
        latitude1 = math.radians(lat)
        longtitude1 = math.radians(long)
        #Changed Code
        latLong = self.read_from_file()
        #Changed Code
        lat = latLong[0]
        long = latLong[1]
        x1 = lat[0:2]
        x2 = lat[2:9]
        lat = float(x1) + float(x2)/60
        y1 = long[0:3]
        y2 = long[3:10]
        long = float(y1) + float(y2)/60
        latitude2 = math.radians(lat)
        longtitude2 = math.radians(long)
        #latitude2 = float(latLong[0])/100
        #longtitude2 = float(latLong[1])/100
        #Changed Code
        cord1 = (latitude1,longtitude1)
        cord2 = (latitude2,longtitude2)
        distance = geopy.distance.geodesic(cord1, cord2).m
        #distance = geopy.distance.vincenty(cord1, cord2).m
        return distance


    ###################################
    # This function returns an error
    # message based on the distance
    #
    # Return: None
    ###################################
    def distance_check(self):
        distance_to_sender = self.calculate_dist_gps()
        print("Distance is:")
        print(distance_to_sender)
        print("\n\r")
        if distance_to_sender < 5:
            print("TURN AROUND")
            print("Distance is to low!")
