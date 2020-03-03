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
    c = randomColor()
    counter = 0
    direction = True
    rect0 = [O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,c,c,O,O,O,
             O,O,O,c,c,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O]
    c = randomColor()
    rect1 = [O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O,
             O,O,c,c,c,c,O,O,
             O,O,c,O,O,c,O,O,
             O,O,c,O,O,c,O,O,
             O,O,c,c,c,c,O,O,
             O,O,O,O,O,O,O,O,
             O,O,O,O,O,O,O,O]
    c = randomColor()
    rect2 = [O,O,O,O,O,O,O,O,
             O,c,c,c,c,c,c,O,
             O,c,O,O,O,O,c,O,
             O,c,O,O,O,O,c,O,
             O,c,O,O,O,O,c,O,
             O,c,O,O,O,O,c,O,
             O,c,c,c,c,c,c,O,
             O,O,O,O,O,O,O,O]
    c = randomColor()
    rect3 = [c,c,c,c,c,c,c,c,
             c,O,O,O,O,O,O,c,
             c,O,O,O,O,O,O,c,
             c,O,O,O,O,O,O,c,
             c,O,O,O,O,O,O,c,
             c,O,O,O,O,O,O,c,
             c,O,O,O,O,O,O,c,
             c,c,c,c,c,c,c,c]
    rects = [rect0,rect1,rect2,rect3]
    while True:
        sense.set_pixels(rects[counter])
        if direction:
            counter += 1
        else:
            counter -=1
        if counter == 0:
            direction = True
        elif counter == 3:
            direction = False
        time.sleep(1)
        
    
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()





