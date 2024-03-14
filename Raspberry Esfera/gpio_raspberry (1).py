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

Atuador_1_A = 20
Atuador_1_B = 21
Atuador_2_A = 16
Atuador_2_B = 12
Motor_A = 19
Motor_B = 26
Ima_A = 13
Ima_B = 6
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

#         if (a == 11):
# 
#             print("AVANÇO MOTOR!!")
#             #Write_Velocity(DXL_ID_1, MAX_VEL)
#             GPIO.output(Motor_A, GPIO.HIGH)
#             GPIO.output(Motor_B, GPIO.LOW)
#             flag_f = True
#             ms_f = time_ns()
# 
#             if (flag_f == True):
#                 print("motor fechando")
# 
#                 if(time_ns()-ms_f > 1200000000 and flag_2 == False):  # 2s
#                     ms_f = time_ns()
#                     GPIO.output(Motor_A, GPIO.LOW)
#                     GPIO.output(Motor_B, GPIO.LOW)
#                     # Write_Velocity(DXL_ID_1, MAX_VEL)
#                     ms_a = time_ns()
#                     flag_2 = True
#                     flag_f = False
# 
#             # if(flag_2 == True and time_ns()-ms_f > 1400000000):  # 2s
            #     GPIO.output(Motor_A, GPIO.LOW)
            #     GPIO.output(Motor_B, GPIO.LOW)
            #     flag_f = False
            #     flag_2 = False
        if(a == 11):
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

        elif(a == 10):
            print("recuar_motor")
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
                
        elif(a == 21):
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

        elif(a == 22):
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
 

        # if(a == 10):
        #     print("AVANÇO MOTOR!!")
        #     if (flag== False):
        #         GPIO.output(Motor_A, GPIO.HIGH)
        #         GPIO.output(Motor_B, GPIO.LOW)
        #         flag = True
        #         ms = time_ns()

        #     if (flag == True):
        #         if(time_ns()-ms > 2000000000):
        #             print("off-1")
        #             GPIO.output(Motor_A, GPIO.LOW)
        #             GPIO.output(Motor_B, GPIO.LOW)
        #             flag = False

        # elif(a == 11):
        #     print("RECUO MOTOR!!")
        #     if(flag2== False):
        #         GPIO.output(Motor_A, GPIO.LOW)
        #         GPIO.output(Motor_B, GPIO.HIGH)
        #         flag2 = True
        #         ms = time_ns()

        #     if (flag2 == True):
        #         if(time_ns()-ms > 100000000):
        #             print("off-2")
        #             GPIO.output(Atuador_1_A, GPIO.LOW)
        #             GPIO.output(Atuador_1_B, GPIO.LOW)
        #             flag2 = False

        # elif(a == 10):
        #     print("recuar_motor")
        #     GPIO.output(Atuador_1_B, GPIO.HIGH)
        #     GPIO.output(Atuador_1_A, GPIO.LOW)

        elif(a == 12):
            print("atuador_on")
            GPIO.output(Atuador_1_A, GPIO.HIGH)
            GPIO.output(Atuador_1_B, GPIO.LOW)

        elif(a == 13):
            print("atuador_off")
            GPIO.output(Atuador_1_A, GPIO.LOW)
            GPIO.output(Atuador_1_B, GPIO.HIGH)

        elif(a == 14):
            print("MAG_ON")
            GPIO.output(Ima_A, GPIO.HIGH)
            GPIO.output(Ima_B, GPIO.LOW)

        elif(a == 15):
            print("MAG_OFF")
            GPIO.output(Ima_A, GPIO.LOW)
            GPIO.output(Ima_B, GPIO.LOW)

        

        a = 5

except KeyboardInterrupt:
    pass

GPIO.cleanup()
