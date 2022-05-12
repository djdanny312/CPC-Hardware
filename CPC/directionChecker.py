from ultrasonic1 import distance1
from ultrasonic2 import distance2
from requesters import pushParkCount
import time
from variables import parking_id,distance_to_detect

global count

count = 0


def dirCheck():
    global count
    dirFlag = 0
    dist1 = distance1()
    dist2 = distance2()
    flag1 = False
    flag2 = False
            
    if dist1<= distance_to_detect and flag2 == False:
                #check if sensor 2 is active
        print("Flag 1 active")
        flag1 = True
        time.sleep(1)
        dist1 = distance1()
        dist2 = distance2()
        if dist2<= distance_to_detect and flag1 == True:
            print("flag 1 and flag 2 activated")
            tenter=time.time()
            time.sleep(3)
            flag2 = True
            dist1 = distance1()
            dist2 = distance2()
            dirFlag=1
            if dist1> distance_to_detect and flag2 == True:
                #vehicle has entered, flag 1 off
                print("Flag 1 off, flag 2 on")
                flag1 = False
                time.sleep(1)
                dist1 = distance1()
                dist2 = distance2()
                if dist2 > distance_to_detect:
                    flag2 = False
                    texit = time.time()
                    #vehicle succesfully entered
                    count+=1
                    print("Someone entered, the count is ",count)
                    print("The direction vehicle entered is: ", dirFlag)
                    time.sleep(5)
                    pushParkCount(count)
                    return count
                            
                        
    if dist2<= distance_to_detect:
        print("Flag 2 activated")
        flag2 = True
        time.sleep(1)
        dist1 = distance1()
        dist2 = distance2()
        if dist1<= distance_to_detect and flag2 == True:
            print("EXIT: Flag 2 and Flag 1 activated")
            tenter = time.time()
            time.sleep(3)
            flag1 = True
            dist1 = distance1()
            dist2 = distance2()
            if dist2> distance_to_detect and flag1 == True:
                print("EXIT: Flag 2 off, flag 1 on")
                flag2 = False
                time.sleep(1)
                dist1 = distance1()
                dist2 = distance2()
                dirFlag=-1
                if dist1> distance_to_detect:
                    flag1 = False
                    texit= time.time()
                            
                    count-=1
                    if count<0:
                        count=0
                    print("Someone exited, the count is ",count)
                    print("The direction vehicle entered is: ", dirFlag)
                    pushParkCount(count)
                    time.sleep(5)
                    return count
                            