#******************BIBLIOTECAS************************************************************************

import os
import RPi.GPIO as GPIO
import time

#*****************ATIVACAO GPIO************************************************************************

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BUZZER = 25
LED = 7
#IMA = 17
ATUADOR1 = 2
ATUADOR2 = 3

GPIO.setup(BUZZER,GPIO.OUT)
GPIO.output(BUZZER,GPIO.LOW)

GPIO.setup(ATUADOR1,GPIO.OUT)
GPIO.output(ATUADOR1,GPIO.LOW)

GPIO.setup(ATUADOR2,GPIO.OUT)
GPIO.output(ATUADOR2,GPIO.LOW)

GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.HIGH)

#GPIO.setup(IMA,GPIO.OUT)
#GPIO.output(IMA,GPIO.HIGH)

f=open ("/home/pi/Desktop/lora.txt","w+")
f.truncate(0)

#*****************WHILE PRINCIPAL********************************************

print("aguardando sinal")

while True:
    
    f=open ("/home/pi/Desktop/lora.txt","r")
    content = f.read()

#************************LIGA LAVADORA***********************************

    if content == "1":
        print("Liga lavadora")

        #GPIO.output(BUZZER,GPIO.HIGH)
        #time.sleep(0.1)
        #GPIO.output(BUZZER,GPIO.LOW)

        #avanco do atuador - liga lavadora
	GPIO.output(ATUADOR1,GPIO.LOW)
	GPIO.output(ATUADOR2,GPIO.HIGH)
        #time.sleep(3)

        f=open ("/home/pi/Desktop/lora.txt","w+")
        f.truncate(0)

        print("Finalizado, aguardando novo sinal")

#************************DESLIGA LAVADORA***********************************

    if content == "2":
        print("Desliga lavadora")

        #GPIO.output(BUZZER,GPIO.HIGH)
        #time.sleep(0.1)
        #GPIO.output(BUZZER,GPIO.LOW)

        #recuo do atuador - desliga lavadora
	GPIO.output(ATUADOR1,GPIO.HIGH)
	GPIO.output(ATUADOR2,GPIO.LOW)
        #time.sleep(3)

        f=open ("/home/pi/Desktop/lora.txt","w+")
        f.truncate(0)

        print("Finalizado, aguardando novo sinal")
     