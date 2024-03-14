#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from dynamixel_sdk import *
import os
import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT) # ATUDOR AVANÇO
GPIO.setup(24, GPIO.OUT) # ATUADOR RECUO
GPIO.setup(22, GPIO.OUT) # SUPORTE ON/OFF


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
# AS VEZES O U2D2 E A LORA SE EMBARALHAM NO INICIO DO PI ENTÃO É BOM DEIXAR DE MODO A NÃO DAR ERRO!

DEVICENAME = '/dev/ttyUSB0'
DEVICENAME_2 = '/dev/ttyUSB1'
lora_receiver2 = serial.Serial('/dev/ttyUSB1', 115200)
lora_receiver = serial.Serial('/dev/ttyUSB0', 115200)

# Control table address dynamixel
TORQUE_ENABLE_T = 64
OPERATION_MODE = 11
GOAL_VELOCITY = 104
VELOCITY_LIMIT = 44
ADDR_PRO_GOAL_POSITION = 116
ADDR_PRO_PRESENT_POSITION = 132

# CONFIGURATION DYNAMIXEL
PROTOCOL_VERSION = 2.0
BAUDRATE = 57600

DXL_ID_1 = 1  

# CONFIGURATION ENABLES
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
VELOCITY_CONTROL = 1
POSITION_CONTROL = 3

# CRITERIOS DE SEGURANÇA
MAX_VEL = 1000
MIN_POS = 0
MAX_POS = 4000

packetHandler = PacketHandler(PROTOCOL_VERSION)


def port_conf(DXL_ID):

	portHandler = PortHandler(DEVICENAME)
	lora_receiver = serial.Serial('/dev/ttyUSB1', 115200)

	if portHandler.openPort():
		print('sucessed to open the port')
    #	print("Succeeded to open the port")

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

	dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_DISABLE)

	if dxl_comm_result != COMM_SUCCESS:
		lora_receiver = serial.Serial('/dev/ttyUSB0', 115200)
		portHandler.closePort()
		print("saindo!")
		# exit(1)
		portHandler = PortHandler(DEVICENAME_2)

		if portHandler.openPort():
			print("Succeeded to open the port")
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

		dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_1, TORQUE_ENABLE_T, TORQUE_DISABLE)

		if dxl_comm_result != COMM_SUCCESS:
			print("deu problema , não trocou!")

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
#     print(f'disabel torque == {a}')
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
        print(f'Velocity mode -> id={DXL_ID}')

    # Changing the velocity limit to close to maximum
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
        portHandler, DXL_ID, VELOCITY_LIMIT, MAX_VEL)

    # Enable torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_ENABLE)


def Set_Operation_Mode_Position(DXL_ID):

    # Changing Operation Mode to velocity mode
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, OPERATION_MODE, POSITION_CONTROL)

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print(f'Position mode -> id={DXL_ID}')

    # Enable torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, TORQUE_ENABLE_T, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    else:
        print('toruq enable')


def Write_Velocity(DXL_ID, vel):

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
        print(f'Torque has been successfully turn off! , ID_{DXL_ID}')

	#portHandler, lora_receiver = port_conf(DXL_ID_1)

	#SINAL VISUAL DO SUCESSO!

portHandler, lora_receiver = port_conf(DXL_ID_1)
Set_Operation_Mode_Velocity(DXL_ID_1)
Write_Velocity(DXL_ID_1,MAX_VEL)
sleep(2)
Write_Velocity(DXL_ID_1,0)


#Set_Operation_Mode_Position(DXL_ID_1)
#Write_position(DXL_ID_1, MIN_POS)
#sleep(3) 
#Write_position(DXL_ID_1, MAX_POS)
#sleep(3)

flag= False
flag_a= False
flag_f= False
flag_2 =False

while True:
	recebe = lora_receiver.readline()
	a = int(recebe.decode("utf8"))
    #a = recebe.decode("utf8")
	print(a)
       
	if (a == 11 and flag == False ) :

		print("AVANÇO MOTOR!!")
		Write_Velocity(DXL_ID_1, MAX_VEL)
		flag_f=True
		ms_f = time_ns()

	if (flag_f == True):
		print("motor fechando")

		if(time_ns()-ms_f > 12000000000 and flag_2 == False): #2s
			ms_f = time_ns()
			Write_Velocity(DXL_ID_1,MAX_VEL)
			GPIO.output(23, GPIO.HIGH)
			ms_a= time_ns()
			flag_a= True
			flag_2= True
			print("segunda rodada!")

		if(flag_2 == True and time_ns()-ms_f > 14000000000): #2s
			Write_Velocity(DXL_ID_1,0)
			flag_f = False
			flag_2 = False


	elif(a == 10):
		print("recuar_motor")
		Write_Velocity(DXL_ID_1, -150)
		flag=True
		ms = time_ns()
		#sleep(3)

	if (flag == True ):
		if(time_ns()-ms > 8000000000): #2s
			Write_Velocity(DXL_ID_1,0)
			flag = False
		
		
	elif(a == 12 and flag_a== False):
		print("atuador_on")
		ms_a = time_ns()
		GPIO.output(24, GPIO.HIGH)
		flag_a= True
		print("atuador_on_3")
       
	elif(a == 13 and flag_a == False):
		print("atuador_off")
		ms_a= time_ns()
		GPIO.output(23, GPIO.HIGH)
		flag_a= True
	
	elif(a == 14):
		print("MAG_ON")
		GPIO.output(22, GPIO.HIGH)
		sleep(0.1)

	elif(a == 15):
		print("MAG_OFF")
		GPIO.output(22, GPIO.LOW)
		Write_Velocity(DXL_ID_1, 0)
		sleep(0.1)

	elif (flag_a== True):
		if(time_ns()-ms_a > 750000000): #2s
			flag_a = False
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.LOW)

	# else:	
	# 	print("off")
	# 	GPIO.output(23, GPIO.LOW)
	# 	GPIO.output(24, GPIO.LOW)
		         
	a=5

Disable_Torque(DXL_ID_1)
# Close port
portHandler.closePort()
print("Succeeded to close the port")


############################################################################
#FOR FURTHER USE
""" 
    # for i in range(0, 100):
    #     recebe = lora_receiver.readline()
    #     print(f'{recebe.decode("utf8")}')
    #     time.sleep(0.2)

     GPIO.output(24, GPIO.HIGH)
    sleep(3)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    sleep(3)
    GPIO.output(23, GPIO.LOW)
    # sleep(3) 

    # Disable_Torque(DXL_ID_1)
    # Set_Operation_Mode_Velocity(DXL_ID_1)
    # Write_Velocity(DXL_ID_1,500)
    # sleep(3)
    # Write_Velocity(DXL_ID_1,-500)
    # sleep(3)
    # Write_Velocity(DXL_ID_1,0)
    # sleep(3) """