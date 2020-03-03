from sense_emu import SenseHat
import sys
import time
import random

sense = SenseHat()


def main():
    sense.clear()
    r = [255,0,0]
    v = [255,226,196]
    b = [0,0,255]
    O = [0,0,0]
    mario = [O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,r,r,O,O,O,
             O,O,O,r,r,r,O,O,
             O,O,O,v,v,O,O,O,
             O,O,O,v,v,O,O,O,
             O,O,O,v,O,O,O,O,
             O,O,O,b,b,O,O,O]
    
    mariojump =[O,O,O,r,r,O,O,O,
             O,O,O,r,r,r,O,O,
             O,O,O,v,v,O,O,O,
             O,O,O,v,v,O,O,O,
             O,O,O,v,O,O,O,O,
             O,O,O,b,b,O,O,O,
             O,O,O,b,b,O,O,O,
             O,O,O,b,b,b,v,O]
    
    while True:
        sense.set_pixels(mario)
        event = sense.stick.wait_for_event()
        if(event.action == 'released' and event.direction == 'up'):
            sense.set_pixels(mariojump)
            time.sleep(0.5)
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()


