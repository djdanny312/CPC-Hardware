from CPC.ultrasonic1 import distance1
from CPC.ultrasonic2 import distance2
import hashFunc
import scan
import gsm
import buttonInts
#parking exclusive password
salt="this is the salt"
count=0
maxCount=25
if __name__=='__main__':
    #run main program
    
    
    #if count> maxCount do not open ever::
    if count >= maxCount:
        print("Closed")
    
    #while loop for the ultra sonic sensors, AIM for efficiency    
    while(True):
        count = directionChecker()
        #if second Ultrasensor is HIGH(distance less than 50) gsm open arm..TODO
        d1 = distance1()
        d2 = distance2()
        if d2<50:
            callGSM()    
            
    #Interrupt, activate scan, decode and gsm 
        if count<maxCount:
            #process to open gate
        else:
            continue
    except KeyboardInterrupt:
        print("Keyboard Exception catched.")
    


