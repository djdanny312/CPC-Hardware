from ultrasonic1 import distance1
from ultrasonic2 import distance2
from directionChecker import dirCheck
from scanner import scan
from btconnect import executeBT
from variables import distance_to_detect
import buttonInts

if __name__=='__main__':
    #run main program
    try:
        

        #while loop for the ultra sonic sensors   
        while(True):
            dirCheck()
            dir2= distance2()
            #if second Ultrasensor is HIGH(distance less than 50) open arm 
            if dir2<=distance_to_detect:
                executeBT()
                
                    
            
    except KeyboardInterrupt:
        print("Keyboard Exception catched.")
    


