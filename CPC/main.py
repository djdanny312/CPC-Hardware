from ultrasonic1 import distance1
from ultrasonic2 import distance2
from directionChecker import dirCheck
from scanner import scan


if __name__=='__main__':
    #run main program
    try:
        import buttonInts

        #while loop for the ultra sonic sensors, AIM for efficiency    
        while(True):
            dirCheck()
            #if second Ultrasensor is HIGH(distance less than 50) gsm open arm..TODO          
            
    except KeyboardInterrupt:
        print("Keyboard Exception catched.")
    


