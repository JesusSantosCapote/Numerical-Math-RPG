import msvcrt
import time
def timed_imput(message : str = ">>>", wait_time = 30):
    entrance=""
    print(message)    
    endind_time = time.time() + wait_time
    while time.time() < endind_time:            
        if msvcrt.kbhit():
            char = msvcrt.getche().decode('ASCII')
            if char == "\r": 
                return entrance   
            else:
                entrance += char
    return None

#string = timed_imput()
#if string == None:
#    print("Es igual a None")
#if string == "":
#    print("Es igual a cadena vacía")
