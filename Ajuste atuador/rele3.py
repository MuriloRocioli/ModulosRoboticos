import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#canal 20 e 21 - rele de alimentacao
#canal 17 e 27 - rele de chaveamento

print("inicio")

# Set up the GPIO channels
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(20,GPIO.LOW)
GPIO.setup(21,GPIO.LOW)

time.sleep(0.05)

GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

time.sleep(0.05)

GPIO.setup(20,GPIO.HIGH)
GPIO.setup(21,GPIO.HIGH)