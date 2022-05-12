#timer
import time
from threading import Timer
from variables import minutes_for_timer
from requesters import pushParkCount
from directionChecker import refresh 
#using thread to run events concurrently
def timedRefresh():
    #function to execute when timer is done
    def timeout():
        print("timer over")
        refresh()

    t = Timer(minutes_for_timer*60, timeout)
    t.start()
    print(t.active_count)
    print(t.current_thread)
    t.join()
