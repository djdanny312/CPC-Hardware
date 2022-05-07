from gpiozero import Button
import scan
import hashFunc


buttonPress=Button(16)

def buttonInterrupt():
    #turn on camera,
    
    data = scan(True,10)
    toCompare = hashFunc("salt")
    if data in toCompare:
        callGSM()
    else:
        print("Code does not match")

buttonPress.when_pressed = buttonInterrupt