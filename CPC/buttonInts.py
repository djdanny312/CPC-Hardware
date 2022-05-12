from gpiozero import Button
import RPi.GPIO as GPIO
from scanner import scan
from hashFunc import hashFunction
from requesters import getParkCount,getParkInfo,getParkPass
from btconnect import executeBT
from variables import parking_id,camera_timeout
from leds import redLed,greenLed
import time


#GPIO for push button
buttonPress=Button(16)
#Set led ligh as an Output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def buttonInterrupt():
    
    print("button pressed\n")
    #try getting information depending on the parking id, if there is no existing parking,
    #it will give a Type Error which is handled by exiting the interrupt
    try:
        park_info = getParkInfo(parking_id)
    
        count = park_info["occupancy"]
        max_count = park_info["max_capacity"]
    except Exception as e:
        print("\nParking not found")
        return
    #if the count is bigger than the Max Count Turn Red Led on(OPTIONAL) return every time and do nothing
    if count >= max_count:
        print("Closed, it is full")
        print("RED LED on")
        redLed()
        return
    #hash function of the specied parking salt and the admin salt function.
    pswd = getParkPass()
    toCompare = hashFunction(pswd)
    adminCompare = hashFunction("yo entro donde quiera")
    print("Hashed Code: ", toCompare)
    print("Admin Hash: ",adminCompare)
    #run scaning algorith and return the data scanned
    data = scan(False,camera_timeout)
    print(data)
    #if the scanned data is the same as the hashed data give access
    if data in toCompare or data in adminCompare:
        print("GREEN LED ON")
        executeBT()
        greenLed()
        return
     #if the scanned data is not the same as the hashed data Turn on Red led
    elif data and data not in toCompare and data not in adminCompare:
        print("Wrong QR code")
        redLed()           
        return
    #else the scanned data is empty as there was no QR code scanned, Turn on Red led
    else:
        print("TIMEOUT: There was no code")
        redLed()
        return

buttonPress.when_pressed = buttonInterrupt