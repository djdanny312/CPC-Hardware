#python sms send script
import time
import sys
import serial

def callGSM():
    mobile = "+34674855906"
    phone = serial.Serial()

    phone.port="/dev/ttyS0"
    phone.baudrate=115200
    phone.xonoff=False
    phone.rtscts=False
    phone.bytesize= serial.EIGHTBITS
    phone.parity= serial.PARITY_NONE
    phone.stopbits = serial.STOPBITS_ONE

    phone.open()
    phone.flushInput()
    phone.flushOutput()
    time.sleep(0.5)
    phone.write(b'AT\r\n')
    time.sleep(0.5)
    phone.write(b'ATD+34674855906;\r\n')
    out=""
    time.sleep(1)
    while phone.inWaiting()>0:
        out +=phone.read(1)
        if out !="":
            print(">>" + out)





