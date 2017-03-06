from pygame import mixer
import time
import datetime
from threading import Timer

now = datetime.datetime.now()
print(now)

compareTime = datetime.datetime(2017, 3, 4, 5, 00, 00, 00)
print compareTime

delta_t = compareTime-now
secs = delta_t.seconds+1

def test():
    print "test"
    mixer.init()
    mixer.music.load("im_shipping_up_to_boston.wav")

    running = True
    while running:
        mixer.music.play()
        time.sleep(1000)

t = Timer(secs, test)
t.start()
