#!/usr/bin/env python
import RPi.GPIO as GPIO
import os, time
import pibooth
import pibooth_notifications
import threading


## not quite sure which way I want to thread this


## define threaded functions

#def picture_thread():

#def notification_thread():

## an added main funtion would make sense here 
## this would use the functions above and probably
## a cleaned up version of what is below as well 
## the idea being that the button spawns the notifications
## and the initiation of the command line utility 
## which displays a preview and then takes a picture

## for each button click (that doesn't overlap another's process)
## the process should take a variable number of photos likely 3 or 4
## the notifications should also let the user know how many pictures
## are taken and how many are left to take 



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


