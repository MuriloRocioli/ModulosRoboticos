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

GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.HIGH)

#********************WHILE PRINCIPAL************************************************************************************

while True:

#********************LEITURA LORA E FUNCAO CASE*******************************************************

    recebe = lora_receiver.readline()
    a = str(recebe.decode("utf8"))
    a = int(a)

    if(a == 1):
        print("Sobe desce 1 BOLA")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("1")
        print("SINAL DA LORA RECEBIDO")

    if(a == 2):
        print("Diagonal XIS")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("2")

    if(a == 3):
        print("TRIANG")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("3")

    if(a == 4):
        print("QUAD")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("4")

    if(a == 5):
        print("Esquerda")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("5")

    if(a == 6):
        print("Direita")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("6")

    if(a == 7):
        print("Cima")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("7")

    if(a == 8):
        print("Baixo")
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("8")
        

        