import time
import os

light = True

def lights_on():
    global light
    light = True
    print(light)
    return light

def lights_off():
    global light
    light = False
    print(light)
    return light

def lights_toggle():
    global light
    light = not light
    print(light)
    return light