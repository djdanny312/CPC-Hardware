from CPC.ultrasonic1 import distance1
from CPC.ultrasonic2 import distance2
import time

count = 0
maxCount = 0

if __name__=='__main__':
    try:
        while True:
            dist1 = distance1()
            dist2 = distance2()
            if dist1<=20:
                #check if sensor 2 is active
                if dist2<=20:
                    count+=1
                    print("Someone entered, the count is ",count)
            elif dist2<=20:
                if dist1<=20:
                    count-=1
                    print("Someone exited, the count is ",count)   
            else:
                continue 
    except KeyboardInterrupt:
        print("Keyboard Interrupted")


# def checkEntry_Exit():
#     flag1=False
#     flag2=False

#     if dist1<=30:
#      #check if vehicle is entering
#         time.sleep(0.5)
#         flag1=True
#         if dist2<=30 and flag1 == True:
#             flag2=True
#             time.sleep(0.05)
#         return True
#     else:
#         return False







