#!/usr/bin/env python

# This is a simple an elegant & simple implementation of an rotary decoder WITHOUT the need of debouncing!! 
# Its based on the wonderful explanation and example from Matthias Hertel at https://github.com/mathertel/RotaryEncoder
# I also did a interrupt port of his code to Arduino, pm me at Twitter LSA232 if you need some

import RPi.GPIO as GPIO
import time

pin1 = 20 # GPIO 20
pin2 = 16 # GPIO 16
counter = 0
oldState = 0 # save last state

GPIO.setmode(GPIO.BCM) # choose by gpio numbers
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    global oldState
    global counter
    sig1 = GPIO.input(pin1)
    sig2 = GPIO.input(pin2)
    tmpState = sig1 + (sig2 * 2)
    if tmpState == 3 and oldState == 0:
        counter -= 1
        print counter
    if tmpState == 2 and oldState == 1:
        counter += 1
        print counter
    oldState = tmpState

GPIO.add_event_detect(pin1, GPIO.BOTH, callback=my_callback)


try:
    while True: # run until CTRL-C
        # nothing to do
        pass

finally:
    GPIO.cleanup()
