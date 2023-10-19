import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#canal 20 e 21 - rele de alimentacao
#canal 17 e 27 - rele de chaveamento

print("inicio")

# Set up the GPIO channels
GPIO.setup(16,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.setup(22,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(10,GPIO.IN,GPIO.PUD_DOWN)

GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.HIGH)

flag = 0
flag2 = 0

print("aguardando fim de curso")

#BUZZER


#a = open("/home/pi/Desktop/bipe.txt","r")

#arq = a.read()

#print(arq)

#if arq == "":

#    a = open("/home/pi/Desktop/bipe.txt","w+")
#    a.write("3")

#    a = open("/home/pi/Desktop/bipe.txt","w+")
#    a.write("3")

#    print("sucesso")

print("acionamento")
GPIO.output(25,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)



