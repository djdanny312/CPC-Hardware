import serial as ser

gms = ser.Serial("/dev/ttyS0",115200,timeout= 0.5)
gsm.flush()

def sendSMS(msg):
    print("Sneding SMS\n")
    gsm.write(b'AT+CMFG=1\r\n')
    sleep(0.5)
    gsm.write(b'AT+CMGS=\"')
    serialcmd = args["mobile-Number"]
    gsm.write(b'\"\r\n')
    sleep(0.5)
    data = msg
    gsm.write(data.encode())
    gsm.write(b'\x1A')  #CNTRL-Z
    sleep(3)

sendSMS("CPC says Hi")