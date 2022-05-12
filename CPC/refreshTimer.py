#timer
import time
from threading import Timer
from variables import minutes_for_timer
from requesters import pushParkCount
from directionChecker import refresh 
#using thread to run events concurrently
def timedRefresh():
    #function to execute when timer is done
    try:
        def timeout():
            print("timer over")
            refresh()

        t = Timer(0.05*60, timeout)
        t.start()
        
        t.join()
    except Exception as e:
        return e
