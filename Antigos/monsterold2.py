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
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(12,GPIO.OUT)

#GPIO.setup(15,GPIO.IN,GPIO.PUD_DOWN)
#GPIO.setup(19,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(10,GPIO.IN,GPIO.PUD_UP)

GPIO.output(23,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
#GPIO.output(5,GPIO.HIGH)
#GPIO.output(6,GPIO.HIGH)

GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.LOW)
GPIO.output(13,GPIO.LOW)

#FIM DE CURSO 1: NIVEL LOGICO em 6 e INPUT EM 19 (26)
#FIM DE CURSO 2: NIVEL LOGICO em 5 e INPUT EM 15 
#FIM DE CURSO 3 (DE BAIXO): NIVEL LOGICO em 13 e INPUT EM 10 (16)
GPIO.output(12,GPIO.HIGH)

flag = 0
flag2 = 0

print("aguardando fim de curso")

time.sleep(10)

#BUZZER

GPIO.output(16,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(16,GPIO.LOW)


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
    
while True:
    
    i = i+1
    
    #print(GPIO.input(16))
    #print("mais",mais)
    #print("menos",menos)
    
    if GPIO.input(26) == 1: maisa = maisa + 1
    if GPIO.input(26) == 0: menosa = menosa + 1    
    
    if GPIO.input(10) == 1: maisb = maisb + 1
    if GPIO.input(10) == 0: menosb = menosb + 1
    
    #if flag == 0 and ((GPIO.input(15) == 1 or GPIO.input(19) == 1)):
    #if flag == 0 and GPIO.input(19) == 1:
    #if flag == 0 and GPIO.input(19) == 0:
    if i == 25 and flag == 0 and menosa > maisa:

        print("acionamento")
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        
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

    #if (GPIO.input(10) == 1 and flag == 1 and (GPIO.input(22) == 1 or GPIO.input(26) == 1)):
    #if (i == 10 and GPIO.input(16) == 0 and flag == 1):
    if (i == 25 and menosb > maisb and flag == 1):
        
        print("esse e o valor", GPIO.input(16))
        #time.sleep(5)
        
        print("desacionamento")

        flag = 0

        GPIO.output(25,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)

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
        
        mais = 0
        menos = 0
        
        time.sleep(5)


    if i == 25:
        i = 0
        maisa = 0
        maisb = 0
        menosa = 0
        menosb = 0