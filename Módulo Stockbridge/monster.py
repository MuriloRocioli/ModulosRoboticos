import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIOs 9-10-18-15

print("inicio...aguardar delay")

# Set up the GPIO channels
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# NIVEL LOGICO PARA ACIONAR FIM DE CURSO
GPIO.setup(9,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

GPIO.setup(5,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(10,GPIO.IN,GPIO.PUD_UP)

#HIGH PORQUE RELE ACIONA POR NIVEL LOGICO BAIXO

GPIO.output(15,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)

#LOW PORQUE RESISTORES INTERNOS SAO PULL UP

GPIO.output(9,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
GPIO.output(8,GPIO.HIGH) #PWM CANAL 1 MONSTERSHIELD - PINO 4

flag = 0
flag2 = 0

print("aguardando fim de curso")

time.sleep(10)

a = open("/home/pi/Desktop/bipe.txt","r")

arq = a.read()

print(arq)

if arq == "":

    a = open("/home/pi/Desktop/bipe.txt","w+")
    a.write("0")

    a = open("/home/pi/Desktop/bipe.txt","w+")
    a.write("0")
    
    a = open("/home/pi/Desktop/bipe.txt","r")
    arq = a.read()
    
    if arq == "0":
        a = open("/home/pi/Desktop/bipe.txt","w+")
        a.truncate(0)
        print("sucesso")
    
i = 0
maisa = 0
menosa = 0
maisb = 0
menosb = 0
    
flag2 = 0
    
while True:
    
    i = i+1
    
    if GPIO.input(10) == 1: maisa = maisa + 1
    if GPIO.input(10) == 0: menosa = menosa + 1    
    
    if GPIO.input(5) == 1: maisb = maisb + 1
    if GPIO.input(5) == 0: menosb = menosb + 1
    
    #print(GPIO.input(10))
    
    if i == 10 and flag == 0 and menosa > maisa:

        print("acionamento")
        GPIO.output(18,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        
        flag = 1
        
        #ENVIO SINAL LORA

        a = open("/home/pi/Desktop/bipe.txt","w+")

        a.write("0")
        a.truncate(0)
        
        time.sleep(0.05)
        
        a = open("/home/pi/Desktop/bipe.txt","w+")
        a.write("a")
        
        a = open("/home/pi/Desktop/bipe.txt","r")        
        arq = a.read()
        
        if arq != "a":
            a = open("/home/pi/Desktop/bipe.txt","w+")
            a.write("a")
            print("reescrito")
        
        time.sleep(7)

    if (i == 25 and menosb > maisb and flag == 1 and flag2 == 0):
        
        #print("esse e o valor", GPIO.input(16))
        #time.sleep(5)
        
        print("desacionamento")

        flag = 0
        flag2 = 1

        GPIO.output(18,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)

        a = open("/home/pi/Desktop/bipe.txt","w+")

        a.write("0")
        a.truncate(0)
        
        time.sleep(0.05)
        
        a = open("/home/pi/Desktop/bipe.txt","w+")
        a.write("b")
        
        a = open("/home/pi/Desktop/bipe.txt","r")        
        arq = a.read()
        
        if arq != "b":
            a = open("/home/pi/Desktop/bipe.txt","w+")
            a.write("b")
            print("reescrito")
        
        time.sleep(5)


    if i == 25:
        i = 0
        maisa = 0
        maisb = 0
        menosa = 0
        menosb = 0