#!/usr/bin/env python
import RPi.GPIO as GPIO
import os, time
import pibooth

#adjust for where your switch is connected
buttonPin = 18 
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)
initialpress = 1
#initialise a previous input variable to 1 (assume button pressed last)
prev_reading = 1
while True:
  #take a reading
  reading = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_reading) and reading):
    if initialpress:
      initialpress = 0
    else:
     pibooth.takePicture(preview=True) 
  #  print("Button pressed")
  #update previous input
  prev_reading = reading
  #slight pause to debounce
  time.sleep(0.05)


