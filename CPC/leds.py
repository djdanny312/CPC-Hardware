import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def greenLed():
    print("GREEN LED ON")
    GPIO.output(6,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(6,GPIO.LOW)
    
    
def redLed():
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(5,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(5,GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(5,GPIO.LOW)
