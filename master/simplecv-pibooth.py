from SimpleCV import Camera, Display
from datetime import datetime, timedelta
import datetime as dt

class Countdown(object):

    font_size = 180
    save_directory = "pictures"

    countdown_target = dt.MINYEAR
    ONE_SECOND = timedelta(0,1)
    TWO_SECONDS = timedelta(0,2)
    THREE_SECONDS = timedelta(0,3)
    position_cache = dict()
    take_picture = False

    def trigger(self, img):
        self.countdown_target = datetime.now() + self.THREE_SECONDS
        layer = img.dl()

    def paint(self, img):
        now = datetime.now()
        if now > self.countdown_target:
            if self.take_picture:
                self.take_picture = False
                filename = self.save_directory + "/%s.png" % now.isoformat()
                img.save(filename)
                print("saved to " + filename)
            return

        self.take_picture = True
        layer = img.dl()
        if self.countdown_target - now > self.TWO_SECONDS:
            self.__draw_text(layer, "3")
        elif self.countdown_target - now > self.ONE_SECOND:
            self.__draw_text(layer, "2")
        elif self.countdown_target > now:
            self.__draw_text(layer, "1")

    def __draw_text(self, layer, text):
        layer.setFontSize(self.font_size)

        # calculate and store positions so we only need to calculate once
        if text not in self.position_cache:
            (text_width,text_height) = layer.textDimensions(text)
            self.position_cache[text] = ((layer.width - text_width)/2,
                                         (layer.height - text_height)/2)

        layer.text(text, self.position_cache[text], color=(255,255,255), alpha=100)


disp = Display()
cam = Camera()
countdown = Countdown()

temp_trigger = datetime.now()
while True:
    img = cam.getImage()
    # TODO: remove time-based temp_trigger (takes a picture every 10 seconds) in 
    # favor of raspberry pi button-press event
    if datetime.now() > temp_trigger:
        countdown.trigger(img)
        temp_trigger = temp_trigger + timedelta(0,10)
    countdown.paint(img)
    img.show()
