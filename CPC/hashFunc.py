from datetime import *
from hashlib import sha256

def hashFunction(salt):
    now = datetime.now()
    
    toHash= str(now.day) + str(now.hour) + str((now.minute -5)//5)
    prev = sha256((toHash+salt).encode("utf-8")).hexdigest()[:10]
    
    toHash= str(now.day) + str(now.hour) + str(now.minute//5)
    curr = sha256((toHash+salt).encode("utf-8")).hexdigest()[:10]
    
    result = (prev,curr)
    return result
    

if __name__=="__main__":
    tup = hashFunction("salt")
    print(tup)