import notify2

# initial testing of using python's notify2 to notify 
# photobooth users that they should get ready for a photo
# and how close they are to getting their photos taken

def countdown_notify( seconds=3 ):
     notify2.init("pi booth")

     #notify2.Notification("Countdown Starts now","Prepare your smile :)").show()
     #notify2.Notification("Countdown Starts now","Prepare your smile :)").close()

     x = seconds
     cdtext =""
     while x>-1:
          if x == 3:
            cdtext = "Lights!"
          elif x == 2:
            cdtext = "Camera!"
          elif x == 1:
            cdtext = "Picture Time!"
          elif x == 0:
            cdtext = "Smile!!"
          else:
            cdtext = "Get ready to smile :)"
          notify2.Notification(str(x),cdtext).show()
          notify2.Notification(str(x),cdtext).close()
          x = x - 1
