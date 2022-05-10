import serial as ser
import time

gsm = ser.Serial("/dev/ttyS0",115200,timeout= 0.5)
gsm.flush()

def sendSMS(msg):
    print("Sending SMS\n")
    gsm.write(b'AT+CMFG=1\r\n')
    time.sleep(0.5)
    gsm.write(b'AT+CMGS="+17872374230"')
    gsm.write(b'\"\r\n')
    time.sleep(0.5)
    data = msg
    gsm.write(data.encode())
    gsm.write(b'\x1A')  #CNTRL-Z
    time.sleep(3)
    print("message sent")
sendSMS("CPC says Hi")