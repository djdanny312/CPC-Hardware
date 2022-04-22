from datetime import *

def hashFunc():
    now = datetime.now()
    toHash= str(now.day) + str(now.hour) + str(now.minute)
    
    if now.minute % 5==0:
        hashed = str(hash(toHash))
        if hashed<0:
            hashed = hashed * -1
        return hashed
    
        
    else:
        print("Not a multiple of 5, rounding... \n")
        rounded = 5 * round( hash(toHash) / 5)
        if rounded<0:
            rounded = rounded * -1
        return str(rounded)
if __name__=="__main__":
    print(hashFunc())