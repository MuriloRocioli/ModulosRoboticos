import serial

arduino = serial.Serial('/dev/ttyUSB1', 115200)

while True:
    recebe = arduino.readline()
    #print(recebe)
    a= int(recebe.decode("utf-8"))
    print(a)
    
    if (a ==10):
        print("hello beatyful!!")
    elif(a == 11):
        print("recuar")
    #if a >=(10):
    #    print("i' doing it!!!")

