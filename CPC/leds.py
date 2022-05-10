import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

print("GREEN LED ON")
GPIO.output(6,GPIO.HIGH)
time.sleep(1.5)
GPIO.output(6,GPIO.LOW)

time.sleep(1.5)

print("RED LED ON")
GPIO.output(5,GPIO.HIGH)
time.sleep(1.5)
GPIO.output(5,GPIO.LOW)
        
time.sleep(1.5)
