from datetime import *

def hashFunc():
    now = datetime.now()
    toHash= str(now.day) + str(now.hour) + str(now.minute)
    
    if now.minute % 5==0:
        return str(hash(toHash))
        
    else:
        print("Not a multiple of 5, rounding... \n")
        rounded = 5 * round( hash(toHash) / 5)
        return str(rounded)
