import sys
from datetime import datetime
from yeelight import Bulb

hour = datetime.now().hour
minute = datetime.now().minute

if len(sys.argv) == 3:
  hour = int(sys.argv[1])
  minute = int(sys.argv[2])

bulb = Bulb('192.168.2.189')

if hour==8: 

  if minute <= 5:
    print("green")
    bulb.set_rgb(0, 255, 0)
    quit()
  
  if minute <= 10:
    print("orange")
    bulb.set_rgb(255, 153, 51)
    quit()

  if minute <= 15:
    print("red")
    bulb.set_rgb(255, 0, 0)
    quit()

if hour==21:
  bulb.set_rgb(255, 178, 102)
  quit()

if hour==22:
  bulb.set_rgb(255, 128, 0)
  quit()

if hour==23:
  bulb.set_rgb(255, 0, 0)
  quit()
