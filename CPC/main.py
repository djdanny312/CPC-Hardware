from CPC.ultrasonic1 import distance1
from CPC.ultrasonic2 import distance2
import hashFunc
import scan

if __name__=='__main__':
    #run main program
    dist1 = distance1()
    dist2 = distance2()
    count=0
    maxCount=0
    baseHash = hashFunc()
    valid = False
    try:
        while True:
            if dist1<=20:
                #turn on camera
                recievedHash= scan(True,10)
                if baseHash==recievedHash:
                    #allow acces to the user
                    valid=True
                    #TODO send signal, GSM or Bluetooth.
                else:
                    valid = False
                    #DO not open gate
            
    
            
    except KeyboardInterrupt:
        print("Keyboard Exception catched. ")
    


