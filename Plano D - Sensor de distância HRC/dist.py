#*******************DECLARACAO BIBLIOTECAS*************************

from dronekit import connect, Command, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import RPi.GPIO as GPIO
import serial
import os
import math

#*******************DECLARACAO VARIAVEIS****************************

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 6
ECHO = 5
#TRIG = 24
#ECHO = 23

BUZZER = 25
LED = 26
maxTime = 0.04

#Aciona LED

GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.HIGH)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

des = 0
med = 0
i = 0

#*************************************LEITURA DISTANCIA****************************

while True:

	    #print(med+des)
	    i = i + 1
        
	    GPIO.output(TRIG,False)
	    #print("Waiting For Sensor To Settle")
	    time.sleep(0.01)

	    GPIO.output(TRIG,True)

	    time.sleep(0.00001)

	    GPIO.output(TRIG,False)

	    pulse_start = time.time()
	    timeout = pulse_start + maxTime
	    while GPIO.input(ECHO) == 0 and pulse_start < timeout:
	    	pulse_start = time.time()

	    pulse_end = time.time()
	    timeout = pulse_end + maxTime
	    while GPIO.input(ECHO) == 1 and pulse_end < timeout:
	    	pulse_end = time.time()

	    pulse_duration = pulse_end - pulse_start
	    distance = pulse_duration * 17000
	    distance = round(distance, 2)

	    if distance <0:

		    distance = 0

	    if distance >400:

		    distance = 400

	    distance = int(distance)
	    
	    if i==1:
                v1 = distance
	    if i==2:
                v2 = distance
	    if i==3:
                v3 = distance
	    if i==4:
                v4 = distance
                
	    if i==5:
                v5 = distance
                
                #med = statistics.mean([v1, v2, v3, v4, v5])
                
                med = 1.0*(v1+v2+v3+v4+v5)/5
                
                des = 1.0*((v1-med)*(v1-med)+(v2-med)*(v2-med)+(v3-med)*(v3-med)+(v4-med)*(v4-med)+(v5-med)*(v5-med))/4 
                
                des =  math.sqrt(des)
                
                i = 0
                
                              
                if v5 <= (med+des) and v5 >= (med-des):
                
                        a = open("/home/pi/Desktop/bipe.txt","w+")

                        if v5 <= 100:

                            a.write("1")

                        elif v5 > 150:

                            a.write("3")
		    
                        elif v5 < 150 and v5 > 100:

                            a.write("2")

                        print("Distance:",v5,"cm")
                        

	    #dist = str(distance)

            #f = open("/home/pi/Desktop/dist.txt","w+")

	    #f.write(dist)
	    
	    #print(dist)



