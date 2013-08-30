import notify2

# initial testing of using python's notify2 to notify 
# photobooth users that they should get ready for a photo
# and how close they are to getting their photos taken

def countdown_notify( seconds=3 ):
     notify2.init("pi booth")

     notify2.Notification("Count Down","Countdown starts now").show()

     x = seconds
     while x>-1:
          notify2.Notification("Count Down",str(x)).show()
          x = x - 1
