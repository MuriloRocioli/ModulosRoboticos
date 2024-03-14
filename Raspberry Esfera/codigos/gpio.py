import RPi.GPIO as GPIO
from time import *


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


for i in range(1, 10):
    GPIO.output(24, GPIO.HIGH)
    sleep(3)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    sleep(3)
    GPIO.output(23, GPIO.LOW)
    # sleep(3)
