from yeelight import Bulb
import time
bulb = Bulb('192.168.2.189')
bulb.set_rgb(250, 100, 200)
time.sleep(10)
bulb.set_rgb(50, 50, 70)
time.sleep(10)
bulb.set_rgb(255, 80, 80)
