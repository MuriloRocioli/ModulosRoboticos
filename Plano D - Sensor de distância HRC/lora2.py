#********************IMPORTACAO BIBLIOTECAS******************************************************************************************************************************

import os
import serial
import RPi.GPIO as GPIO
import time

#********************VERIFICACAO DA PORTA PARA A LORA************************************************************************************

if os.name == 'nt':
    import msvcrt

    def getch():
        return msvcrt.getch().decode()

else:
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()

    lora_receiver = serial.Serial('/dev/ttyUSB0', 115200)
    print("inicia programa")

#********************DEFINE PORTAS GPIOS****************************************************************

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 16
flag = 0

GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.HIGH)

#********************WHILE PRINCIPAL************************************************************************************

while True:

#********************ESCRITA NA LORA******************
        
    f = open("/home/pi/Desktop/bipe.txt","r")
    bipe = f.read()
    
    f = open("/home/pi/Desktop/bipe2.txt","r")
    bipe2 = f.read() 

    if bipe == "1":
        lora_receiver.write(str.encode("1"+"/r/n"))
    if bipe == "3":
        lora_receiver.write(str.encode("3"+"/r/n"))
    if bipe == "2":
        lora_receiver.write(str.encode("2"+"/r/n"))
        
        
        
        
        
    #if bipe == "3" and bipe2 == "3":
    #    lora_receiver.write(str.encode("3"+"/r/n"))
    #if bipe == "2" or bipe2 == "2":
    #    if bipe == "1" or bipe2 == "1":
    #        flag = 1
    #        lora_receiver.write(str.encode("1"+"/r/n"))
    #    else:
    #        lora_receiver.write(str.encode("2"+"/r/n"))
    #if (bipe == "1" or bipe2 == "1") and flag == 0:
    #    lora_receiver.write(str.encode("1"+"/r/n"))    
    #flag = 0
                 



        

        