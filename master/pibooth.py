import datetime, time, os
from subprocess import call
from time import sleep

def timestamped(fname, fmt='%Y_%m_%d_%H%M%S.{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def timeFmt( fmt='%Y-%m-%d-%H:%M:%S'):
    return datetime.datetime.now().strftime(fmt)

def takePicture(delay = 0, preview = False):
    args = ["raspistill"]
    args.append("-f" if preview else "-n")
    if delay != 0:
        args.append("-t " + str(delay))
    args.append("-o " + timestamped("photo.jpg"))
    args.append("-w " + str(1280))
    args.append("-h " + str(1024))
    args.append("-op " + str(212))
    call([' '.join(args)], shell=True)


"""
# TODO: count down of 3 2 1 should also start at around 5 seconds ?
print("3!")
sleep(1)
print("2!")
sleep(1)
print("1!")
sleep(1)
print("Say cheese!")
takePicture(preview=True)
print("Picture taken!")
takePicture()
print("ninja picture taken!")
"""
