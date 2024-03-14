# gpio raspberry
import serial
import RPi.GPIO as GPIO
from time import *
import time

#####ESPERA PARA ABERTURA DO PROGRAMA DA LORA

sleep(2)

######

flaginst = 0

flag = False
flag_2= False
flag_a1 = False
flag_a2 = False
flag_2 = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

lora_receiver = serial.Serial('/dev/ttyUSB0', 115200)

# DEFINE AS SAIDAS

Atuador_1_A = 20 #ATUADOR MENOR
Atuador_1_B = 21 #ATUADOR MENOR
Atuador_2_A = 16 #ATUADOR MAIOR
Atuador_2_B = 12 #ATUADOR MAIOR
Motor_A = 19 #MOTOR PARAFUSADEIRA
Motor_B = 26 #MOTOR PARAFUSADEIRA
Ima_A = 13 #FECHADURA MAGNETICA
Ima_B = 6 #FECHADURA MAGNETICA
PW1 = 17
PW2 = 27
# SETA TODAS AS SAIDAS

GPIO.setup(Atuador_1_A, GPIO.OUT)
GPIO.setup(Atuador_1_B, GPIO.OUT)
GPIO.setup(Atuador_2_A, GPIO.OUT)
GPIO.setup(Atuador_2_B, GPIO.OUT)
GPIO.setup(Motor_A, GPIO.OUT)
GPIO.setup(Motor_B, GPIO.OUT)
GPIO.setup(Ima_A, GPIO.OUT)
GPIO.setup(Ima_B, GPIO.OUT)
GPIO.setup(PW1, GPIO.OUT)
GPIO.setup(PW2, GPIO.OUT)
# INICIA TODOS EM OFF

GPIO.output(Atuador_1_B, 0)
GPIO.output(Atuador_2_A, 0)
GPIO.output(Atuador_1_A, 0)
GPIO.output(Atuador_2_B, 0)
GPIO.output(Motor_A, 0)
GPIO.output(Motor_B, 0)
GPIO.output(Ima_A, 0)
GPIO.output(Ima_B, 0)

GPIO.output(PW1, 1)
GPIO.output(PW2, 1)

#ENTRADA DIGITAL

GPIO.setup(17,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.OUT)

GPIO.output(27,1)

################PREPARACAO ARQUIVO TEXTO BIPE TXT

a = open("/home/pi/Desktop/bipe.txt","r")

arq = a.read()

#print(arq)

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
        print("sucesso bipe")


################WHILE PRINCIPAL

try:
    while True:

        file = open("/home/pi/Desktop/lora.txt","r")
        a = file.read()
        #print(a)

        if(GPIO.input(17) == 1 and flaginst == 0):
        #if(a == "3"):
            print("procedimento instalacao esfera")
            
            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

            print("envia sinal sonoro LORA")

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

            print("aciona_motor")
            GPIO.output(Motor_A, GPIO.HIGH)
            GPIO.output(Motor_B, GPIO.LOW)

            sleep(5)

            print("desliga_motor")
            GPIO.output(Motor_A, GPIO.LOW)
            GPIO.output(Motor_B, GPIO.LOW)

            print("atuador menor off")
            GPIO.output(Atuador_1_A, GPIO.HIGH)
            GPIO.output(Atuador_1_B, GPIO.LOW)

            print("Atuador maior_OFF")
            GPIO.output(Atuador_2_A, GPIO.HIGH)
            GPIO.output(Atuador_2_B, GPIO.LOW)

            sleep(5)

            print("envia sinal sonoro finalizou")

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

            flaginst = 1

        if(a == "5"):
            print("MAG_ON")
            GPIO.output(Ima_A, GPIO.HIGH)
            GPIO.output(Ima_B, GPIO.LOW)

            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

        if(a == "6"):
            print("MAG_OFF")
            GPIO.output(Ima_A, GPIO.LOW)
            GPIO.output(Ima_B, GPIO.LOW)

            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

        if(a == "9"):
            print("atuador_off")
            GPIO.output(Atuador_1_A, GPIO.HIGH)
            GPIO.output(Atuador_1_B, GPIO.LOW)

            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

        if(a == "4"):
            print("atuador_on")
            GPIO.output(Atuador_1_A, GPIO.LOW)
            GPIO.output(Atuador_1_B, GPIO.HIGH)
            
            sleep(1)
            
            GPIO.output(Atuador_1_A, GPIO.LOW)
            GPIO.output(Atuador_1_B, GPIO.LOW)            

            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

        if(a == "2"):
            print("recuar_motor")
            # Write_Velocity(DXL_ID_1, -150)
 
            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)
 
            GPIO.output(Motor_A, GPIO.HIGH)
            GPIO.output(Motor_B, GPIO.LOW)
            #flag_2 = True
            #ms = time()
            
            sleep(1)
            
            GPIO.output(Motor_A, GPIO.LOW)
            GPIO.output(Motor_B, GPIO.LOW)



        #if (flag_2 == True):
            #print(time() - ms)
            #if(time()-ms > 2):
                #print("time-ok")
                #GPIO.output(Motor_A, GPIO.LOW)
                #GPIO.output(Motor_B, GPIO.LOW)
                #flag_2 = False

        if(a == "1"):
            
            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)
            
            print("avancar_motor")
            # Write_Velocity(DXL_ID_1, -150)
            GPIO.output(Motor_A, GPIO.LOW)
            GPIO.output(Motor_B, GPIO.HIGH)
            
            sleep(1)

            GPIO.output(Motor_A, GPIO.LOW)
            GPIO.output(Motor_B, GPIO.LOW)
            
            #flag = True
            #ms = time()

        #if (flag == True):
            #print(time() - ms)
            #if(time()-ms > 1):
                #print("time-ok")
                #GPIO.output(Motor_A, GPIO.LOW)
                #GPIO.output(Motor_B, GPIO.LOW)
                #flag = False
                
        if(a == "8"):
            print("AT2_OFF")
            
            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

            GPIO.output(Atuador_1_A, GPIO.LOW)
            GPIO.output(Atuador_1_B, GPIO.LOW)

            GPIO.output(Atuador_2_A, GPIO.HIGH)
            GPIO.output(Atuador_2_B, GPIO.LOW)
            #flag_a1 = True
            #ms = time()

        #elif (flag_a1 == True):
            #print(time() - ms)
            #if(time()-ms > 0.5):
                #print("time-ok")
                #GPIO.output(Atuador_2_A, GPIO.LOW)
                #GPIO.output(Atuador_2_B, GPIO.LOW)
                #flag_a1 = False

        elif(a == "7"):
            print("AT2_ON")
            
            a = open("/home/pi/Desktop/lora.txt","w+")
            a.truncate(0)

            GPIO.output(Atuador_1_A, GPIO.LOW)
            GPIO.output(Atuador_1_B, GPIO.LOW)
            
            GPIO.output(Atuador_2_A, GPIO.LOW)
            GPIO.output(Atuador_2_B, GPIO.HIGH)
            #flag_a2 = True
            #ms = time()

        #elif (flag_a2 == True):
            #print(time() - ms)
            #if(time()-ms > 0.5):
                #print("time-ok")
                #GPIO.output(Atuador_2_A, GPIO.LOW)
                #GPIO.output(Atuador_2_B, GPIO.LOW)
                #flag_a2 = False

        a = "99"

except KeyboardInterrupt:
    pass

GPIO.cleanup()
