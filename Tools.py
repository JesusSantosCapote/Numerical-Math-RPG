import msvcrt
import time
from matplotlib import pyplot
from armors import *
from PIL import Image
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

def graph_function (func, range, selected_color):
    pyplot.plot(range, [func(i) for i in range])
    pyplot.axhline(0, color=selected_color)
    pyplot.axvline(0, color=selected_color)
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)
    pyplot.savefig("output.png")
    pyplot.show()