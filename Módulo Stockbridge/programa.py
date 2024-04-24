#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from dynamixel_sdk import *
import os
import RPi.GPIO as GPIO
from time import *
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#******************GPIO 2-3-13-17-19-22-23-24-25-26-27

GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)

GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.LOW)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.output(21,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.HIGH) #enable
GPIO.output(27,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

if os.name == 'nt':
    import msvcrt

    def getch():
        return msvcrt.getch().decode()
else:
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()


# TODO ORGANIZAR COM TRY AND ECEPT HERE
DEVICENAME = '/dev/ttyUSB0'
DEVICENAME_2 = '/dev/ttyUSB1'
lora_receiver2 = serial.Serial('/dev/ttyUSB1', 115200)
lora_receiver = serial.Serial('/dev/ttyUSB0', 115200)

# Control table address
TORQUE_ENABLE_T = 64
OPERATION_MODE = 11
GOAL_VELOCITY = 104
VELOCITY_LIMIT = 44
ADDR_PRO_GOAL_POSITION = 116
ADDR_PRO_PRESENT_POSITION = 132

# CONFIGURATION DYNAMIXEL
PROTOCOL_VERSION = 2.0
BAUDRATE = 57600

DXL_ID_1 = 1  # tracao
DXL_ID_2 = 2  # marico
DXL_ID_3 = 3 

# CONFIGURATION ENABLES
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
VELOCITY_CONTROL = 1
POSITION_CONTROL = 3

# CRITERIOS DE SEGURANÇA
MAX_VEL = 1000
MIN_POS = 0
MAX_POS = 4000

#VELOCIDADE MOTOR

velo = 1000

packetHandler = PacketHandler(PROTOCOL_VERSION)

flag = 0

#########INICIALIZADOR ARQUIVO TEXTO######

a = open("/home/pi/Desktop/porta.txt","r")

arq = a.read()

print(arq)

if arq == "":

    a = open("/home/pi/Desktop/porta.txt","w+")
    a.write("0")

    a = open("/home/pi/Desktop/porta.txt","w+")
    a.write("0")
    
    a = open("/home/pi/Desktop/porta.txt","r")
    arq = a.read()
    
    if arq == "0":
        a = open("/home/pi/Desktop/porta.txt","w+")
        a.truncate(0)
        print("sucesso")

def port_conf(DXL_ID):

    portHandler = PortHandler(DEVICENAME)
    lora_receiver = serial.Serial('/dev/ttyUSB1', 115200)

    if portHandler.openPort():
        print("Succeeded to open the port")

        #ENVIO SINAL LORA

        f = open("/home/pi/Desktop/porta.txt","w+")

        f.write("0")
        f.truncate(0)
        
        time.sleep(0.05)
        
        f = open("/home/pi/Desktop/porta.txt","w+")
        f.write("/dev/ttyUSB1")
        
        f = open("/home/pi/Desktop/porta.txt","r")        
        arq = f.read()
        
        if arq != "/dev/ttyUSB1":
            f = open("/home/pi/Desktop/porta.txt","w+")
            f.write("/dev/ttyUSB1")
            print("reescrito")

    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()

    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()

    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_DISABLE)

    if dxl_comm_result != COMM_SUCCESS:
        lora_receiver = serial.Serial('/dev/ttyUSB0', 115200)
        portHandler.closePort()
        print("saindo!")
        # exit(1)
        portHandler = PortHandler(DEVICENAME_2)

        if portHandler.openPort():
            print("Succeeded to open the port")

            #ENVIO SINAL LORA

            f = open("/home/pi/Desktop/porta.txt","w+")

            f.write("0")
            f.truncate(0)
            
            time.sleep(0.05)
            
            f = open("/home/pi/Desktop/porta.txt","w+")
            f.write("/dev/ttyUSB0")
            
            f = open("/home/pi/Desktop/porta.txt","r")        
            arq = f.read()
            
            if arq != "/dev/ttyUSB0":
                f = open("/home/pi/Desktop/porta.txt","w+")
                f.write("/dev/ttyUSB0")
                print("reescrito")

        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()

        if portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
            quit()

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, DXL_ID_1, TORQUE_ENABLE_T, TORQUE_DISABLE)

        if dxl_comm_result != COMM_SUCCESS:
            print("deu ruim , não trocou!")

    return portHandler, lora_receiver


# def INITIAL_CONIFG():

#     if portHandler.openPort():
#         print("Succeeded to open the port")
#     else:
#         print("Failed to open the port")
#         print("Press any key to terminate...")
#         getch()
#         quit()

#     if portHandler.setBaudRate(BAUDRATE):
#         print("Succeeded to change the baudrate")
#     else:
#         print("Failed to change the baudrate")
#         print("Press any key to terminate...")
#         getch()
#         quit()
#     a = Disable_Torque(DXL_ID_1)
#     print('disabel torque == {a}')
#     if a == 1:
#         if portHandler.closePort():
#             print("close port")
#             Wrong_connection()


def Set_Operation_Mode_Velocity(DXL_ID):

    # Changing Operation Mode to velocity mode
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, OPERATION_MODE, VELOCITY_CONTROL)

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print('Velocity mode -> id={DXL_ID}')

    # Changing the velocity limit to close to maximum
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, DXL_ID, VELOCITY_LIMIT, MAX_VEL)

    # Enable torque
    #dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    #    portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_ENABLE)

    # Enable torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    else:
        print('torque ligado')

def Set_Operation_Mode_Position(DXL_ID):

    # Changing Operation Mode to velocity mode
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, OPERATION_MODE, POSITION_CONTROL)

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print('Position mode -> id={DXL_ID}')

    # Enable torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    else:
        print('torque ligado')


def Write_velocity(DXL_ID, vel):

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, DXL_ID, GOAL_VELOCITY, vel)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


def Write_position(DXL_ID, pos):

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, DXL_ID, ADDR_PRO_GOAL_POSITION, pos)

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


def Disable_Torque(DXL_ID):

    # Disable Dynamixel Torque -- in case pre-enable
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_DISABLE)

    if dxl_comm_result != COMM_SUCCESS:
        print("1-%s" % packetHandler.getTxRxResult(dxl_comm_result))
        # closeport()
        return 1
    elif dxl_error != 0:
        print("2-%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print('Torque has been successfully turn off! , ID_{DXL_ID}')

if __name__ == "__main__":

    portHandler, lora_receiver = port_conf(DXL_ID_1)
    portHandler, lora_receiver = port_conf(DXL_ID_2)
    portHandler, lora_receiver = port_conf(DXL_ID_3)    
    #Set_Operation_Mode_Position(DXL_ID_1)
    #Write_position(DXL_ID_1, MIN_POS)
    #sleep(3)
    #Write_position(DXL_ID_1, MAX_POS)
    #sleep(3)
    Set_Operation_Mode_Velocity(DXL_ID_1)
    Set_Operation_Mode_Velocity(DXL_ID_2)
    Set_Operation_Mode_Velocity(DXL_ID_3)
    
    # for i in range(0, 100):
    #     recebe = lora_receiver.readline()
    #     print('{recebe.decode("utf8")}')
    #     time.sleep(0.2)

    #Disable_Torque(DXL_ID_1)

    #GPIO.output(16,GPIO.HIGH)
    #sleep(0.6)
    #GPIO.output(16,GPIO.LOW)
    print("aguardando pacote")

    #GPIO.setup(20,GPIO.OUT)
    #GPIO.setup(21,GPIO.OUT)
    #GPIO.setup(17,GPIO.OUT)
    #GPIO.setup(27,GPIO.OUT)
    #flag = 0

#    while True:

#	recebe = lora_receiver.readline()
 #       print(recebe)
#        a = str(recebe.decode("utf8"))
#        a = int(a)
#	if(a==6): break

 #   GPIO.output(16,GPIO.HIGH)
 #   sleep(0.3)
 #   GPIO.output(16,GPIO.LOW)

#*********ROTINA MONSTER SHIELD MOTOR 1*******
#GPIO 26 - 19 - 13 - 6 - 17 - 27

print("rotina monster shield")

#ativa pwm motoredutor 1 - pino 5
#GPIO.output(17,GPIO.HIGH)

#ativa pwm motor 1 - pino 6 - GPIO 19
#GPIO.output(26,GPIO.HIGH)

#ativa pwm motor 2 - pino 5 - GPIO 19
#GPIO.output(25,GPIO.HIGH)

#ativa giro horario motoredutor - pino 7
#GPIO.output(22,GPIO.HIGH)
#GPIO.output(27,GPIO.LOW)

#ativa giro horario motor 1 
#GPIO.output(13,GPIO.HIGH)
#GPIO.output(19,GPIO.LOW)

#ativa giro horario motor 2 
#GPIO.output(24,GPIO.HIGH)
#GPIO.output(23,GPIO.LOW)

#sleep(1)

#desativa giro horario motoredutor - pino 7
#GPIO.output(22,GPIO.LOW)
#GPIO.output(27,GPIO.LOW)

#desativa giro horario motor 1
#GPIO.output(13,GPIO.LOW)
#GPIO.output(19,GPIO.LOW)

#desativa giro horario motor 2
#GPIO.output(24,GPIO.LOW)
#GPIO.output(23,GPIO.LOW)

#desativa pwm motoredutor
#GPIO.output(17,GPIO.LOW)

#desativa pwm motor 1
#GPIO.output(26,GPIO.LOW)

#desativa pwm motor 2
#GPIO.output(25,GPIO.LOW)
            
while True:

        #print("inicio while true")
        #if (flag == 0): recebe = lora_receiver.readline()
        #flag = 1
        #recebe = lora_receiver.readline()
        #print(recebe)
        #a = str(recebe.decode("utf8"))
        #a = int(a)
        #print(a)
        #sleep(0.1)

        flag = 1
        #flag2 = 0
        
        file = open("/home/pi/Desktop/lora.txt","r")
        a = file.read()

        if(a == "1" and flag == 1):
            print("avanco motor")

            #ativa pwm motor 1 - pino 6 - GPIO 19
            GPIO.output(26,GPIO.HIGH)

            #ativa pwm motor 2 - pino 5 - GPIO 19
            GPIO.output(17,GPIO.HIGH)

            #ativa giro horario motor 1 
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.HIGH)

            #ativa giro horario motor 2 
            GPIO.output(22,GPIO.LOW)
            GPIO.output(27,GPIO.HIGH)

            sleep(1)

            #desativa giro horario motor 1
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.LOW)

            #desativa giro horario motor 2
            GPIO.output(22,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)

            #desativa pwm motor 1
            GPIO.output(26,GPIO.LOW)

            #desativa pwm motor 2
            GPIO.output(17,GPIO.LOW)

            #TESTE MOTORREDUTOR
            
            #GPIO.output(24,GPIO.LOW)
            #GPIO.output(21,GPIO.HIGH)
            
            #sleep(2)
            
            #GPIO.output(24,GPIO.LOW)
            #GPIO.output(21,GPIO.LOW)          

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)

        if(a == "2" and flag == 1):
            print("recuo motor")

            #ativa pwm motor 1 - pino 6 - GPIO 19
            GPIO.output(26,GPIO.HIGH)

            #ativa pwm motor 2 - pino 5 - GPIO 19
            GPIO.output(17,GPIO.HIGH)

            #ativa giro horario motor 1 
            GPIO.output(19,GPIO.HIGH)
            GPIO.output(13,GPIO.LOW)

            #ativa giro horario motor 2 
            GPIO.output(22,GPIO.HIGH)
            GPIO.output(27,GPIO.LOW)

            sleep(1)

            #desativa giro horario motor 1
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.LOW)

            #desativa giro horario motor 2
            GPIO.output(22,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)

            #desativa pwm motor 1
            GPIO.output(26,GPIO.LOW)

            #desativa pwm motor 2
            GPIO.output(17,GPIO.LOW)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "3" and flag == 1):
            print("instalacao amortecedor")
            
            print("avanco amortecedor")
            sleep(0.1)
            Write_velocity(DXL_ID_3, -1*velo)
            sleep(87)
            Write_velocity(DXL_ID_3, 0)
            
            print("avanco motoredutor")
            sleep(0.1)
            Write_velocity(DXL_ID_1, -1*velo)
            #sleep(74)
            sleep(30)
            Write_velocity(DXL_ID_1, 0)           
            

            print("giro motoredutor")
            #ativa pwm motor 2 - pino 5 - GPIO 19
            #GPIO.output(21,GPIO.HIGH)

            #ativa giro horario motor 2 
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(21,GPIO.LOW)

            sleep(37)
    
            #ativa giro antihorario motor 2 
            GPIO.output(24,GPIO.LOW)
            GPIO.output(21,GPIO.HIGH)

            sleep(0.2)

            #desativa giro motor 2 
            GPIO.output(24,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)           

            #desativa pwm motor 2 - pino 5 - GPIO 19
            #GPIO.output(21,GPIO.LOW)
            
            print("recuo motoredutor")
            sleep(0.1)
            Write_velocity(DXL_ID_1, velo)
            sleep(30)
            Write_velocity(DXL_ID_1, 0)
            
            print("recua pincas")
            sleep(0.1)
            Write_velocity(DXL_ID_2, -1*velo)
            sleep(4.5)
            Write_velocity(DXL_ID_2, 0)

            print("recuo amortecedor")
            sleep(0.1)
            Write_velocity(DXL_ID_3, velo)
            sleep(85)
            Write_velocity(DXL_ID_3, 0)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "4" and flag == 1):
            print("desinstalacao amortecedor")
            
            print("avanco amortecedor")
            sleep(0.1)
            Write_velocity(DXL_ID_3, -1*velo)
            sleep(87)
            Write_velocity(DXL_ID_3, 0)
            
            print("avanco motoredutor")
            sleep(0.1)
            Write_velocity(DXL_ID_1, -1*velo)
            #sleep(74)
            sleep(30)
            Write_velocity(DXL_ID_1, 0)           
            

            print("giro motoredutor")
            #ativa pwm motor 2 - pino 5 - GPIO 19
            #GPIO.output(21,GPIO.HIGH)

            #ativa giro ANTIhorario motor 2 
            GPIO.output(24,GPIO.LOW)
            GPIO.output(21,GPIO.HIGH)

            sleep(37)

            #desativa giro motor 2 
            GPIO.output(24,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)           

            #desativa pwm motor 2 - pino 5 - GPIO 19
            #GPIO.output(21,GPIO.LOW)

            print("avanca pincas")
            sleep(0.1)
            Write_velocity(DXL_ID_2, velo)
            sleep(4.5)
            Write_velocity(DXL_ID_2, 0)

            print("recuo motoredutor")
            sleep(0.1)
            Write_velocity(DXL_ID_1, velo)
            sleep(30)
            Write_velocity(DXL_ID_1, 0)

            print("recuo amortecedor")
            sleep(0.1)
            Write_velocity(DXL_ID_3, velo)
            sleep(85)
            Write_velocity(DXL_ID_3, 0) 

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "5" and flag == 1):
            print("avanco motoredutor")
            sleep(0.1)
            Write_velocity(DXL_ID_1, -1*velo)
            sleep(5)
            Write_velocity(DXL_ID_1, 0)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "6" and flag == 1):
            print("avanco pincas")
            sleep(0.1)
            Write_velocity(DXL_ID_2, velo)
            sleep(0.4)
            Write_velocity(DXL_ID_2, 0)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "7" and flag == 1):
            print("avanco amortecedor")
            sleep(0.1)
            Write_velocity(DXL_ID_3, -1*velo)
            sleep(5)
            Write_velocity(DXL_ID_3, 0)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "8" and flag == 1):
            print("recua pincas")
            sleep(0.1)
            Write_velocity(DXL_ID_2, -1*velo)
            sleep(3.4)
            Write_velocity(DXL_ID_2, 0)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "9" and flag == 1):
            print("recuo motoredutor")
            sleep(0.1)
            Write_velocity(DXL_ID_1, velo)
            sleep(5)
            Write_velocity(DXL_ID_1, 0)

            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        if(a == "0" and flag == 1):
            print("recuo amortecedor")
            sleep(0.1)
            Write_velocity(DXL_ID_3, velo)
            sleep(5)
            Write_velocity(DXL_ID_3, 0)
            
            file = open("/home/pi/Desktop/lora.txt","w+")
            file.truncate(0)
            
        #if(a == "0"):
            #flag2 = 1
            
            #file = open("/home/pi/Desktop/lora.txt","w+")
            #file.truncate(0)