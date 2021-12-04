import RPi.GPIO as GPIO
import time

import sys
import os
sys.path.append(os.path.relpath("modules/manual"))

from setup import *

def pulse_in(pin, level, timeout):
    t0 = time.time()
    
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeout * 0.000001):
            return 0
    
    t0 = time.time()
    
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeout * 0.000001):
            return 0
    
    pulse_time = (time.time() - t0) * 1000000
    
    return pulse_time
    
    
def get_sonar():    
    GPIO.output(trig_pin, GPIO.HIGH)
    
    time.sleep(0.00001)     
    
    GPIO.output(trig_pin, GPIO.LOW) 
    
    ping_time = pulse_in(echo_pin, GPIO.HIGH, timeout)  
    distance = round((ping_time * 340.0 / 2.0 / 10000.0), 2)    
    
    return distance
