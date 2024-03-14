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

#********************DEFINE PORTAS GPIOS****************************************************************

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#####################ROTINA CORRECAO COMANDOS LORA#######################

a = open("/home/pi/Desktop/lora.txt","r")

arq = a.read()

print(arq)

if arq == "":

    a = open("/home/pi/Desktop/lora.txt","w+")
    a.write("0")

    a = open("/home/pi/Desktop/lora.txt","w+")
    a.write("0")
    
    a = open("/home/pi/Desktop/lora.txt","r")
    arq = a.read()
    
    if arq == "0":
        a = open("/home/pi/Desktop/lora.txt","w+")
        a.truncate(0)
        print("sucesso")


#********************WHILE PRINCIPAL************************************************************************************

while True:

#********************LEITURA LORA E FUNCAO CASE*******************************************************

    recebe = lora_receiver.readline()
    a = str(recebe.decode("utf8"))
    a = int(a)

    print(a)

    if(a == 1):
        print("Sobe desce 1 BOLA")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("1")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "1":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("1")
            print("reescrito")
        
#       f = open("/home/pi/Desktop/lora.txt","w+")
#       f.write("1")
        #print("SINAL DA LORA RECEBIDO")

    if(a == 2):
        print("Diagonal XIS")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("2")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("2")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "2":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("2")
            print("reescrito")

    if(a == 3):
        print("TRIANG")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("3")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("3")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "3":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("3")
            print("reescrito")

    if(a == 4):
        print("QUAD")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("4")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("4")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "4":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("4")
            print("reescrito")

    if(a == 5):
        print("Esquerda")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("5")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("5")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "5":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("5")
            print("reescrito")

    if(a == 6):
        print("Direita")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("6")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("6")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "6":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("6")
            print("reescrito")

    if(a == 7):
        print("Cima")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("7")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("7")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "7":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("7")
            print("reescrito")

    if(a == 8):
        print("Baixo")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("8")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("8")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "8":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("8")
            print("reescrito")
        
    if(a == 9):
        print("Baixo")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("9")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("9")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "9":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("9")
            print("reescrito")
        
    if(a == 0):
        print("Baixo")
        #f = open("/home/pi/Desktop/lora.txt","w+")
        #f.write("0")
        
                #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/lora.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/lora.txt","w+")
        f.write("0")
        
        f = open("/home/pi/Desktop/lora.txt","r")        
        arq = f.read()
        
        print("feito")
        
        if arq != "0":
            f = open("/home/pi/Desktop/lora.txt","w+")
            f.write("0")
            print("reescrito")
