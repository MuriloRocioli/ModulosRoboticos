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

    porta = ""
    
    time.sleep(8)
    
while porta == "":
    
    f = open("/home/pi/Desktop/porta.txt","r")
    porta = f.read()
    
    lora_receiver = serial.Serial(porta, 115200)

print('porta recebida')
print(porta)

#********************WHILE PRINCIPAL************************************************************************************

while True:

#********************ESCRITA NA LORA******************
        
    f = open("/home/pi/Desktop/bipe.txt","r")
    bipe = f.read()

    if bipe == "a":
        lora_receiver.write(str.encode("a"+"/r/n"))
        time.sleep(0.05)
        
        print('mensagem enviada 2')
        
        f = open("/home/pi/Desktop/bipe.txt","w+")
        f.truncate(0)
        
    if bipe == "b":
        lora_receiver.write(str.encode("b"+"/r/n"))
        time.sleep(0.05)
        print('mensagem enviada 3')
        
        f = open("/home/pi/Desktop/bipe.txt","w+")
        f.truncate(0)
        
        

        