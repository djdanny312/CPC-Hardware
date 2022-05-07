from datetime import *
from hashlib import sha256

def hashFunc(salt):
    now = datetime.now()
    
    toHash= str(now.day) + str(now.hour) + str((now.minute -5)//5)
    prev = sha256((toHash+salt).encode("utf-8")).hexdigest()
    
    toHash= str(now.day) + str(now.hour) + str(now.minute//5)
    curr = sha256((toHash+salt).encode("utf-8")).hexdigest()
    
    result = (prev,curr)
    return result
    

if __name__=="__main__":
    tup = hashFunc("This is a salt")
    print(tup)