from gpiozero import Button
import RPi.GPIO as GPIO
from scanner import scan
from hashFunc import hashFunction
from requesters import getParkCount,getParkInfo
import time

#GPIO for push button
buttonPress=Button(16)
#Set led ligh as an Output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def buttonInterrupt():
    #using request get information from parking id 5
    print("button pressed")
    park_info = getParkInfo()
    count = park_info["occupancy"]
    max_count = park_info["max_capacity"]
    #TODO, if count is bigger than max_count, do not open
    if count >= max_count:
        print("Closed, it is full")
        print("RED LED on")
        GPIO.output(5,GPIO.HIGH)
        time.sleep(1.5)
        GPIO.output(5,GPIO.LOW)
        
        
    data = scan(False,10)
    toCompare = hashFunction("07b2cc459803eda3730d45013571fc9fdb48d7f07f4cf335716753249a565833")
    adminCompare = hashFunction("adminsalt")
    if data in toCompare or data in adminCompare:
        print("GREEN LED ON")
        GPIO.output(6,GPIO.HIGH)
        time.sleep(1.5)
        GPIO.output(6,GPIO.LOW)
        
    else:
        print("Code does not match")
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

buttonPress.when_pressed = buttonInterrupt