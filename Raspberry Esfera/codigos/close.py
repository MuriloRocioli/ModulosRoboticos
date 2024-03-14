#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from dynamixel_sdk import *
import os
import time

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
lora_receiver = serial.Serial('/dev/ttyUSB1', 115200)
lora_receiver_2 = serial.Serial('/dev/ttyUSB0', 115200)

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

DXL_ID_1 = 1  # trao
DXL_ID_2 = 2  # marico

# CONFIGURATION ENABLES
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
VELOCITY_CONTROL = 1
POSITION_CONTROL = 3

# CRITERIOS DE SEGURANÇA
MAX_VEL = 1000
MIN_POS = 0
MAX_POS = 4000


def port_conf():
    portHandler = PortHandler(DEVICENAME)
    packetHandler = PacketHandler(PROTOCOL_VERSION)

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

    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID_1, TORQUE_ENABLE_T, TORQUE_DISABLE)

    if dxl_comm_result != COMM_SUCCESS:
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

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, DXL_ID_1, TORQUE_ENABLE_T, TORQUE_DISABLE)

        if dxl_comm_result != COMM_SUCCESS:
            print("deu ruim , não trocou!")


port_conf()
