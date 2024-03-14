# gpio raspberry
import serial
import RPi.GPIO as GPIO
from time import *

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

try:
    while True:

        recebe = lora_receiver.readline()
        a = int(recebe.decode("utf8"))
        print(a)

        if(a == 3):
        #if(a == 3):
            print("procedimento instalacao esfera")

        elif(a == 5):
            print("MAG_ON")
            GPIO.output(Ima_A, GPIO.HIGH)
            GPIO.output(Ima_B, GPIO.LOW)

        elif(a == 6):
            print("MAG_OFF")
            GPIO.output(Ima_A, GPIO.LOW)
            GPIO.output(Ima_B, GPIO.LOW)

        elif(a == 9):
            print("atuador_on")
            GPIO.output(Atuador_1_A, GPIO.HIGH)
            GPIO.output(Atuador_1_B, GPIO.LOW)

        elif(a == 0):
            print("atuador_off")
            GPIO.output(Atuador_1_A, GPIO.LOW)
            GPIO.output(Atuador_1_B, GPIO.HIGH)
	    
        if(a == 2):
            print("recuar_motor")
            # Write_Velocity(DXL_ID_1, -150)
            
            GPIO.output(Motor_A, GPIO.HIGH)
            GPIO.output(Motor_B, GPIO.LOW)
            flag_2 = True
            ms = time()

        if (flag_2 == True):
            print(time() - ms)
            if(time()-ms > 2):
                print("time-ok")
                GPIO.output(Motor_A, GPIO.LOW)
                GPIO.output(Motor_B, GPIO.LOW)
                flag_2 = False

        elif(a == 1):
            print("avancar_motor")
            # Write_Velocity(DXL_ID_1, -150)
            GPIO.output(Motor_A, GPIO.LOW)
            GPIO.output(Motor_B, GPIO.HIGH)
            flag = True
            ms = time()

        elif (flag == True):
            print(time() - ms)
            if(time()-ms > 1):
                print("time-ok")
                GPIO.output(Motor_A, GPIO.LOW)
                GPIO.output(Motor_B, GPIO.LOW)
                flag = False
                
        elif(a == 8):
            print("AT2_ON")
            GPIO.output(Atuador_2_A, GPIO.HIGH)
            GPIO.output(Atuador_2_B, GPIO.LOW)
            flag_a1 = True
            ms = time()

        elif (flag_a1 == True):
            print(time() - ms)
            if(time()-ms > 0.5):
                print("time-ok")
                GPIO.output(Atuador_2_A, GPIO.LOW)
                GPIO.output(Atuador_2_B, GPIO.LOW)
                flag_a1 = False

        elif(a == 7):
            print("AT2_OFF")
            GPIO.output(Atuador_2_A, GPIO.LOW)
            GPIO.output(Atuador_2_B, GPIO.HIGH)
            flag_a2 = True
            ms = time()

        elif (flag_a2 == True):
            print(time() - ms)
            if(time()-ms > 0.5):
                print("time-ok")
                GPIO.output(Atuador_2_A, GPIO.LOW)
                GPIO.output(Atuador_2_B, GPIO.LOW)
                flag_a2 = False

        a = 99

except KeyboardInterrupt:
    pass

GPIO.cleanup()
