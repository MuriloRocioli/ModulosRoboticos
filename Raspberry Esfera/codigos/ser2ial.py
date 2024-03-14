import serial

arduino = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    recebe = arduino.readline()
    print(f'{recebe}')
