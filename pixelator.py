from sense_emu import SenseHat
import sys
import time
import random

sense = SenseHat()

def randomColor():
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        return [r,g,b]

def main():
    O = [0,0,0]
    speed = 1
    colors = [O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O]
    
    while True:
        for x in range(64):
            events = sense.stick.get_events()
            for event in events:
                if(event.action == 'released' and event.direction == 'down'):
                    speed += 0.1
                if(event.action == 'released' and event.direction == 'up' and speed > 0.11):
                    speed -= 0.1
            sense.set_pixels(colors)
            colors[x] = randomColor()
            time.sleep(speed)
            if x == 64:
                x=0
            

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()



