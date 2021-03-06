import datetime, time, os
from pibooth_notifications import countdown_notify
from subprocess import call
from time import sleep
import threading

def timestamped(fname, fmt='%Y_%m_%d_%H%M%S.{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def timeFmt( fmt='%Y-%m-%d-%H:%M:%S'):
    return datetime.datetime.now().strftime(fmt)

def takePicture(delay = 0, preview = False):
    args = ["raspistill"]
    args.append("-f" if preview else "-n")
    if delay != 0:
        args.append("-t " + str(delay))
    args.append("-o " + "/home/pi/photos/"+ timestamped("photo.jpg"))
    args.append("-w " + str(1280))
    args.append("-h " + str(1024))
    args.append("-op " + str(190))
    args.append("-vf " )
    call([' '.join(args)], shell=True)



# Threading demo. This method is invoked in another thread
def notifications():
    call('su pi -c "/usr/bin/python /home/pi/projects/pibooth/master/notify_screen.py"', shell=True) 
    #countdown_notify()
    """
    sleep(1)
    print("3!")
    sleep(1)
    print("2!")
    sleep(1)
    print("1!")
    sleep(1)
    """

def picture_with_notification():
    # Kick off the thread
    notifyThread = threading.Thread(target=notifications)
    notifyThread.daemon = True
    notifyThread.start()

    # This is our main thread, fake invoking the raspistill binary
    takePicture(delay=15000,preview=True)
    #print("Invoking raspberry_pi_camera_module")

    #sleep(4)
    #print("Taking picture!")
    #pibooth.takePicture(preview=True)
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
