#Libraries
import RPi.GPIO as GPIO
import time

#Set GPIO Mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Set GPIO Pins
GPIO_TRIGGER = 19
GPIO_ECHO = 26

#Initialize input/output directions
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance1():
    #set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    
    #turn Trigger to low after 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    #timers
    Start = time.time()
    Stop = time.time()
    #save Start timer
    while GPIO.input(GPIO_ECHO)==0:
        Start = time.time()
    #save stop timer
    while GPIO.input(GPIO_ECHO)==1:
        Stop = time.time()
    
    TimeElapsed= Stop - Start
    #calculate the distance by multiplying the sonic speed(34300 cm/s) and divide by due to the time that returns
    distance = (TimeElapsed * 34300) / 2
    
    return distance
