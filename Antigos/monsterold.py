import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#canal 20 e 21 - rele de alimentacao
#canal 17 e 27 - rele de chaveamento

print("inicio")

# Set up the GPIO channels
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.setup(22,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(10,GPIO.IN,GPIO.PUD_DOWN)

GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.HIGH)

flag = 0
flag2 = 0

print("aguardando fim de curso")

while True:
    
    if flag == 0 and ((GPIO.input(22) == 1 or GPIO.input(26) == 1)):

        print("acionamento")
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(24,GPIO.HIGH)
        
        flag = 1
        
        time.sleep(7)

    #if (GPIO.input(10) == 1 and flag == 1 and (GPIO.input(22) == 1 or GPIO.input(26) == 1)):
    if (GPIO.input(10) == 1 and flag == 1):
        print("desacionamento")

        flag = 0

        GPIO.output(25,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)

        time.sleep(3)


